FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python-tk \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev

RUN pip install --no-cache-dir pillow

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
