# Permite execução de scripts apenas nesta sessão
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Ativa o ambiente virtual
& "C:\temp\flask-test\Scripts\Activate.ps1"

# Vai para a pasta do projeto
cd "C:\pyHome\python-flask-api"

# Roda o sistema
python run.py
