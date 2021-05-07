FROM python:3
#WORKDIR /usr/src/app
WORKDIR /code
COPY requirements.txt .
RUN pip install --requirement requirements.txt
# COPY . /tmp/
COPY cowin_v1.py .

CMD ["cowin_v1.py"]
ENTRYPOINT ["python3"]