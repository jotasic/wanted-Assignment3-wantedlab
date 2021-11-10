import csv, re

from django.db                   import connection
from django.db.utils             import OperationalError
from django.core.management.base import BaseCommand

from companies.models            import Company, Tag
from execptions                  import FileExtensionNotMatchError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-p', required=True, type=str, help='Csv file path')

    def handle(self, *args, **options):
        path = options['p']
    
        self.stdout.write(self.style.SUCCESS('[Start] export csv data...'))

        try:
            if not re.match(".*\.csv$", path):
                raise FileExtensionNotMatchError('The file extension is not csv!')

            header = set()
            data   = []

            # csv의 1개의 row에 해당되는 data를 가져와서 딕셔너리 형태로 변환한다.
            # 딕셔너리로 변환 후 row 단위로 안 넣는 이유는 모든 데이터를 순회해야 
            #   어떠한 header 필요한지 알 수 있기 때문이다.
            #  Company : Tag = 1 : N
            for company in Company.objects.prefetch_related('tag_set').all():
                row = {}
                for k, v in company.company_name.items():
                    h      = f'company_{k}'
                    row[h] = v
                    header.add(h)

                for tag in company.tag_set.all():
                    for k, v in tag.tag_name.items():
                        h      = f'tag_{k}'
                        if row.get(h) is None:
                            row[h] = v
                        else:
                            row[h] = row[h]+'|'+v
                        header.add(h)
                        
                data.append(row)

            with open(path, 'w', newline='') as csv_file:
                header = list(header)
                header.sort()
 
                writer = csv.DictWriter(csv_file, fieldnames=header)
                writer.writeheader()

                for r in data:
                    writer.writerow(r)

            self.stdout.write(self.style.SUCCESS('[Success] export csv data...'))
        
        except OSError as err:
            self.stdout.write(self.style.ERROR('OS error: {0}'.format(err)))

        except FileExtensionNotMatchError as err:
            self.stdout.write(self.style.ERROR('File Extension Not Match Error: {0}'.format(err)))

        except BaseException as err:
            self.stdout.write(self.style.ERROR(f'Unexpected {err=}, {type(err)=}'))

        else:
            self.stdout.write(self.style.NOTICE('[Done] export csv data...'))