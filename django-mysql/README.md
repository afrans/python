
## Steps Install using gitbash
```bash
# 1. Criar o projeto Django
# (Opcional, mas recomendado) Criar venv
python -m venv .venv
.venv/Scripts/activate
# 2. Instalar Django e driver MySQL
pip install django mysqlclient # option: PyMySQL
# 3. Criar o projeto Django
django-admin startproject config .
# 4. Apontar o Django para o MySQL do Docker
# Abra o arquivo config/settings.py e encontre a parte DATABASES. Troque pelo seguinte
# 5. Criar uma app alunos
python manage.py startapp alunos
# Agora registre a app em INSTALLED_APPS no config/settings.py
# 6. Criar o modelo (ORM) Aluno, Edite o arquivo alunos/models.py:
# 7. Registrar o modelo no admin
# 8. Criar as tabelas no MySQL (migrations)
# Criar as tabelas padrão do Django
# Criar a tabela alunos_aluno no MySQL dentro do banco curso_db
python manage.py makemigrations
python manage.py migrate
# 9. Criar usuário admin e acessar o painel
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/admin/
```

## Run mysql docker
```bash
cd pasta/onde/está/o/docker-compose/do-mysql
docker compose up -d
```

## Test
```bash
python manage.py shell
Paste script_test_mydql.txt
```
