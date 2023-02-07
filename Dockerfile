FROM python:3.9.1

WORKDIR /PXL_workshop

RUN pip install --upgrade pip


COPY requirements.txt /PXL_workshop/
RUN pip install -r requirements.txt


COPY . /PXL_workshop/

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "localhost:8080"]

