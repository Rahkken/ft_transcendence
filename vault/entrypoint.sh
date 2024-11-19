#!/bin/sh
vault server -dev -dev-listen-address="0.0.0.0:8200" -log-level="info" \
  -dev-root-token-id="roottoken" &

export VAULT_ADDR="http://vault:8200"

echo "Waiting for Vault to be ready..."
until curl -s http://127.0.0.1:8200/v1/sys/health > /dev/null; do
  sleep 1
done

vault kv put secret/django \
  DB_NAME=${POSTGRES_DB} \
  DB_USER=${POSTGRES_USER} \
  DB_PASSWORD=${POSTGRES_PASSWORD} \
  DB_HOST=${POSTGRES_HOST} \
  DB_PORT=${POSTGRES_PORT} \
  SENDGRID_API_KEY=${SENDGRID_API_KEY} \
  SENDGRID_EMAIL=${SENDGRID_EMAIL}

wait