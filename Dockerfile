FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]