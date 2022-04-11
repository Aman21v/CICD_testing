FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install gunicorn
RUN pip install -r req.txt
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
