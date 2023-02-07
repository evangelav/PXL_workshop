FROM python:3.9.1

WORKDIR /PXL_workshop

COPY requirements.txt /PXL_workshop/requirements.txt
WORKDIR /PXL_workshop
RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

COPY . /PXL_workshop/

EXPOSE 8080

CMD  python manage.py runserver localhost:8080

