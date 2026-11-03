FROM python:3.12-slim
WORKDIR /app
COPY --chown=10001:10001 server.py ./server.py
COPY --chown=10001:10001 public ./public
USER 10001:10001
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
CMD ["python", "server.py"]
