# იყენებს Python 3.10-ის ოფიციალურ იმიჯს
FROM python:3.10

# სამუშაო დირექტორიის შექმნა
WORKDIR /app

# ფაილების ასლი
COPY . .

# ბიბლიოთეკების დაყენება
RUN pip install --no-cache-dir -r requirements.txt

# ბოტის გაშვება
CMD ["python", "bot.py"]
