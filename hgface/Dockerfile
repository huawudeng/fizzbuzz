FROM python:3.10.7
ENV PYTHONBUFFERED 1
RUN mkdir /code
ADD ./sentiment /code
WORKDIR /code
RUN pip install --trusted-host pypy.org --trusted-host files.pythonhosted.org -r requirements.txt