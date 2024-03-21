심리테스트를 위한 로컬환경에서의 프로젝트 세팅

1. dockerfile과 requirements.txt를 통한 빌드 성공
    - 하지만 alembic.ini와 env.py의 세부 설정 불가(지식의 부족)
    - 그리하여 로컬환경에서 기본 ini 세팅 후 진행하는것으로 변경
    - 로컬에 postgres를 설치하고 모든 권한을 가진 베이스 유저 생성 성공
    - 로컬기준 alembic 세팅은 성공적!