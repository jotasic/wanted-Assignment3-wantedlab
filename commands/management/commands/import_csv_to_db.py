import csv, re

from django.db                   import connection
from django.db.utils             import OperationalError
from django.core.management.base import BaseCommand

from companies.models            import Company, Tag
from Execptions                  import FileExtensionNotMatchError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-p', required=True, type=str, help='Csv file path')
        parser.add_argument('--clean', required=False, default=False, type=bool, 
                                help='Import after delete all data in database')

    def handle(self, *args, **options):
        path = options['p']

        if options['clean'] :
            self.stdout.write(self.style.SUCCESS('[Start] Delete all data in database...'))
            Company.objects.all().delete()
            Tag.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('[Done] Delete all data in database...'))
    
        self.stdout.write(self.style.SUCCESS('[Start] import csv data...'))

        try:
            if not re.match(".*\.csv$", path):
                raise FileExtensionNotMatchError('The file extension is not csv!')

            with open(path, mode='r') as csv_file:
                reader  = csv.reader(csv_file)
                headers = next(reader, None)
                headers = [col.split('_') for col in headers]
                
                for row in reader:
                    data = {"company" : {}, 'tag' : []}
                    for header, value in zip(headers, row):
                        if header[0] == 'company' and value != '':
                            data['company'][header[1]] = value

                        if header[0] == 'tag':
                            if not data['tag']: 
                                data['tag'] = [{header[1] : n} for n in value.split('|')]
                            else:
                                for d, tag in zip(data['tag'], value.split('|')):
                                    d[header[1]] = tag
                    
                    company = Company.objects.create(company_name=data['company'])

                    for tag in data['tag'] :
                        Tag.objects.create(company=company, tag_name=tag)
                
            self.stdout.write(self.style.SUCCESS('[Success] import csv data...'))
        
        except OSError as err:
            self.stdout.write(self.style.ERROR('OS error: {0}'.format(err)))

        except FileExtensionNotMatchError as err:
            self.stdout.write(self.style.ERROR('File Extension Not Match Error: {0}'.format(err)))

        except BaseException as err:
            self.stdout.write(self.style.ERROR(f'Unexpected {err=}, {type(err)=}'))

        else:
            self.stdout.write(self.style.NOTICE('[Done] import csv data...'))