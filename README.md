# Initial:

- install python3.6
- install node 6.x+


## install python packages:
`pip install -r requirements.txt`

## install node modules:
`npm install`

## install postgres
- add user from config.yaml

Migrate:
```
cd server/
alembic upgrade head
```

# Run:

## Server:
```
server/main.py
```
## Node test
```
npm run test
```
## Git describe in app
```
node index.js
```
## Generate migrations:
```
cd server/
alembic revision --autogenerate -m "migration message"
```

*I used this README.md from my pet-project. in this repo it's useless*

## python linter:
```
flake8 --exclude=./*venv
```