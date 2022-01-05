## download-lambda

AWS Lambda Downloads ZIP / JSON

- AWS CLI
- python3

OBS.: verificar suas credenciais.

### verifique suas credenciais
```bash
aws sts get-caller-identity
```

### lista suas funcões lambda
```bash
aws lambda list-functions
```

### execute o script
```bash
python3 download_lambda.py
```
OBS.: gera um arquivo *data_file.json* com informações atuais e salva todos os zip no diretório *lambda_functions/*
