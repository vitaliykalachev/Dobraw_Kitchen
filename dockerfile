# 
FROM python:3.10.4

# 
WORKDIR /Users/new/VSCodeProjects/Fastapi_Kitchen_Dobraw/Dobraw_Kitchen/app

# 
COPY requirements.txt ./

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
