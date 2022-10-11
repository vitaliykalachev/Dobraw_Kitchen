# 
FROM python:3.10.4

# 
WORKDIR /Dobraw_Kitchen/app

# 
COPY ./requirements.txt /Dobraw_Kitchen/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /Dobraw_Kitchen/requirements.txt

# 
COPY ./app /Dobraw_Kitchen/app

# 
CMD ["python", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
