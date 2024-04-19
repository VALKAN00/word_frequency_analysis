FROM python

WORKDIR /app

COPY cloud.py .
COPY paragraphs.txt .

RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt

CMD ["python", "cloud.py"]
