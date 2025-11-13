FROM python:3.9

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Run your pygame app (this opens a window if environment supports GUI)
CMD ["python", "app.py"]
