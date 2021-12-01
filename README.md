# Assignment3-TW-JW-YY

원티드x위코드 백엔드 프리온보딩 과제3
- 과제 출제 기업 정보
  - 기업명 : 원티드랩


## 과제 후기
- https://velog.io/@burnkim61/프리온보딩-과제-3

## 팀 Repository
- https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY


## Members
|이름   |github                   |담당 기능|
|-------|-------------------------|------------------|
|김태우 |[jotasic](https://github.com/jotasic)     |개발 환경설정, 모델링, 회사 추가 api |
|고유영 |[lunayyko](https://github.com/lunayyko)   |회사 검색 api |
|박지원 |[jiwon5304](https://github.com/jiwon5304) |회사 상세 정보 조회 api |


## 과제 내용

<details>
  <summary><b>과제 내용 자세히 보기</b></summary>
<div markdown="1">

> 다음과 같은 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 REST API 서버를 개발해주세요.

- 원티드 선호 기술스택
  - Python flask 또는 fastapi

### [데이터]
- 회사 정보
    - 회사 이름 (다국어 지원 가능)
- 회사 정보 예제
    - 회사 이름 (원티드랩 / Wantedlab)
- 데이터 셋은 원티드에서 제공
- 데이터셋 예제
  - 원티드랩 회사는 한국어, 영어 회사명을 가지고 있습니다. (모든 회사가 모든 언어의 회사명을 가지고 있지는 않습니다.)

|컬럼명 | company_name_ko   | company_name_en | company_name_ja |
|-------|-------------------|-----------------|-----------------|
|내용   | 원티드랩          | wantedlab       |                 |


### [REST API 기능]
- 회사명 자동완성
    - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가

### [개발 조건]
- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.

  </details>
  
## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PostgreSQL 14.0-0064a5?style=for-the-badge&logo=PostgreSQL&logoColor=white"/>&nbsp;
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/SWAGGER-5B8C04?style=for-the-badge&logo=Swagger&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 모델링
<img width="414" alt="Screen Shot 2021-11-10 at 12 23 36 AM" src="https://user-images.githubusercontent.com/8315252/140954209-39b73d6b-2af9-4b7c-b761-265e92f7fe0d.png">



## API
- [Posman Document](https://documenter.getpostman.com/view/16042359/UVC5Enhh)

## 구현 기능
### 회사 추가 기능 - 🙋‍♂️ 담당기능
- POST "/companies"으로 회사를 등록 합니다.
- 생성 성공 시, 생성된 값 중 x-wanted-language 헤더값 으로 지정된, 언어의 대한 값을 리턴합니다.
  
### 회사 검색 기능
- 헤더에 언어정보가 없으면 한국어를 기본값으로 한다
- 헤더의 언어정보를 받아서 해당 언어로 된 회사이름을 검색한다
- 검색결과를 drf serializer를 통해 Json으로 출력한다
- 한 글자만 들어가도 자동완성으로 검색결과를 출력한다

### 회사 상세 정보 조회 기능
- "/companies/회사이름" 으로 회사이름을 입력합니다.
- 헤더값(x-wanted-language)으로 'ko' or 'en' or 'ja' 등을 입력합니다.
- 위의 입력정보로 회사이름과 해당언어의 태그를 조회합니다.
- 검색된 회사가 없는 경우는 404에러를 반환합니다.


### Model에 Jsonfield를 사용한 이유 및 발생 한 문제점
- 새로운 언어가 추가 될 수 있으므로, 언어 별로 컬럼값을 고정 할 수 없다고 판단하였습니다.
- 하지만 Jsonfield는 json형태로 저장하면 새로운 언어가 추가되어도 상관없으니 대처가 가능하다고 생각했습니다.

(저장 예시 - Company Model)

|id| company_name                                               |
|--|------------------------------------------------------------|
| 1| {"ko": "라인 프레쉬", "tw": "LINE FRESH", "en": "LINE FRESH"} |                     

- 또한 Jsonfield 내의 있는 key 값들을 이용해서 ORM을 작성할 수 있으므로 model 구조의 단순성과 검색의 편의성 두가지를 가질 수 있다고 판단하였습니다.
- 하지만 기능 중 `2. 회사 이름으로 회사 검색` 은 영어로된 url이 들어와도, header가 한국어면 한국어의 대한 결과를 출력하는 유형이였습니다.
- 맨 처음에 이 기능을 header가 한국어면 `무조건 한국어로된 url이` 들어온다고 생각했습니다. 그래서 검색조건도 특정 언어를 포함 시켜서 검색을 했습니다.

(검사 조건 예시)
```python
company = Company.objects.get(company_name__ko="라인 프레쉬")
```

- 이 점이 문제가 되는 이유는 첫번째로 언어가 row마다 다를 수 있습니다. 그러므로 특정언어의 대한 조건으로 검색 못합니다.

- 또한 Jsonfield 내의 존재하는 key 를 검사할 방법은 있지만 values를 검사할 수 있는 방법은 없습니다.
  
- 그래서 비슷한 내용이 있는 data를 가져오는 filter를 실행 후, 각각의 결과를 url과 일치하는 지 비교 후, 완전하게 일치하면 찾은 것으로 로직을 변경하기로 하였습니다.
```python
        found_company = None
        companies = Company.objects.filter(company_name__icontains=name)
        for company in companies:
            if name in company.company_name.values():
                found_company = company
                break

        if not found_company:
            raise Http404()

        company_serializer = CompanySerializer(found_company, many=False)
```

- 과제 조건에 따라서 동작하도록 하였지만, 효율성을 따졌을때는 안 좋은 코드를 만들게 되었습니다.
- 추후에는 과제조건을 더욱 면밀히 봐서 이러한 상황을 만들지 않도록 노력해야겠다고 느꼈습니다. 


## 배포정보
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 | http://18.188.189.173:8021/            |    |


## API TEST 방법
1. 우측 링크를 클릭해서 postman으로 들어갑니다. [링크](https://www.postman.com/wecode-21-1st-kaka0/workspace/assignment3-tw-jw-yy)

2. 정의된 SERVER_URL이 올바른지 확인 합니다. (18.188.189.173:8021)
![image](https://user-images.githubusercontent.com/8219812/140955077-cf4755ad-7575-44fa-a865-5be478fc71a1.png)


3. 만약 Send버튼이 비활성화가 될 시 fork를 이용해서 해당 postman project를 복사해서 시도하길 바랍니다.
![image](https://user-images.githubusercontent.com/8219812/139912241-d6cb5831-23e8-4cbb-a747-f52c42601098.png)


## 설치 및 실행 방법
<details>
  <summary><b>설치 및 실행  자세히 보기</b></summary>
<div markdown="1">
  
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY
    cd Assignment3-TW-JW-YY
    ```
2. 가상 환경을 만들고 프로젝트에 사용한 python package를 받는다.
    ```bash
    conda create --name Assignment3-TW-JW-YY python=3.8
    conda actvate Assignment3-TW-JW-YY
    pip install -r requirements.txt
    ```

3. docker환경 설정 파일을 만든다.
    ### .dockerenv.dev.local
    ```text
    DJANGO_SECRET_KEY = 'django시크릿키'
    ```

4. docker-compose를 통해서 db와 서버를 실행시킨다.
    ```bash
    docker-compose -f docker-compose-dev-local.yml up
    ```
    
5. 만약 백그라운드에서 실행하고 싶을 시 `-d` 옵션을 추가한다.
    ```bash
    docker-compose -f docker-compose-dev-local.yml up -d
    ```

###  배포용 
1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY
    cd Assignment3-TW-JW-YY
    ```

2. docker환경 설정 파일을 만든다.

  
3. 백엔드 서버용 .dockerenv.deploy.backend 파일을 만들어서 안에 다음과 같은 내용을 입력한다. manage.py와 같은 폴더에 생성한다.
    ### .dockerenv.dev_local.backend
    ```text
    DJANGO_SECRET_KEY = 'django시크릿키'
    ```
   
4. DB 용 .dockerenv.deploy.db 파일을 만들어서 안에 다음과 같은 내용을 입력한다. manage.py와 같은 폴더에 생성한다.
  
    ### .dockerenv.deploy.backend
    ```text
      SQL_DATABASE_NAME=db이름
      SQL_USER=db_user이름
      SQL_PASSWORD=db_비밀번호
      DJANGO_SECRET_KEY='django시크릿키'
    ```

    ### .dockerenv.deploy.db
    ```text
     POSTGRES_DB=db이름
     POSTGRES_USER=db_user이름
     POSTGRES_PASSWORD=db_비밀번호
    ```
    
5. docker-compose를 통해서 db와 서버를 실행시킨다.
    
    ```bash
    docker-compose -f docker-compose-deploy.yml up
    ```
    
6. 만약 백그라운드에서 실행하고 싶을 시 `-d` 옵션을 추가한다.
  
    ```bash
    docker-compose -f docker-compose-deploy.yml up -d
    ```
  </details>  
 
## Commands

### import_csv_to_db
csv 파일을 import 한다. 파일 형식은 `wanted_temp_data.csv`를 참조한다.

#### 사용법
```bash
python manage.py import_csv_to_db -p csv_파일경로 --clean=[true or false]
-p : import할 csv 파일의 경로
--clean : import전에 현재 저장되어 있는 데이터를 전부 삭제할 지에 대한 여부 (default value : false)
```
#### 예시
```bash
python manage.py import_csv_to_db -p wanted_temp_data.csv --clean=true

[Start] Delete all data in database...
[Done] Delete all data in database...
[Start] import csv data...
[Success] import csv data...
[Done] import csv data...
```

### export_csv_from_db
csv 파일을 export 한다. 저장되는 파일 형식은 `wanted_temp_data.csv`를 참조한다.

#### 사용법
```bash
python manage.py export_csv_from_db -p csv_파일경로
-p : export할 csv 파일의 경로
```

#### 예시
```bash
python manage.py export_csv_from_db -p export_wanted_temp.csv

[Start] export csv data...
[Success] export csv data...
[Done] export csv data...
```

## 폴더 구조

```bash
├── Dockerfile-deploy
├── Dockerfile-dev-local
├── README.md
├── commands
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   └── management
│       ├── __init__.py
│       └── commands
│           ├── __init__.py
│           ├── import_csv_to_db.py
|           ├── export_csv_from_db.py
│           └── wait_for_db_connected.py
├── companies
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20211108_1550.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers
│   │   ├── __init__.py
│   │   ├── create_serializers.py
│   │   ├── detail_serializers.py
│   │   └── list_serializers.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_create_company.py
│   │   ├── test_detail_company.py
│   │   └── test_search_company.py
│   ├── urls.py
│   └── views
│       ├── __init__.py
│       ├── create_views.py
│       ├── detail_views.py
│       └── list_views.py
├── config
│   └── nginx
│       └── nginx.conf
├── docker-compose-deploy.yml
├── docker-compose-dev-local.yml
├── ex_test_app.py
├── execptions.py
├── manage.py
├── pull_request_template.md
├── requirements.txt
├── wanted_temp_data.csv
└── wantedlab
    ├── __init__.py
    ├── asgi.py
    ├── settings
    │   ├── base.py
    │   ├── deploy.py
    │   └── dev_local.py
    ├── urls.py
    └── wsgi.py
```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
