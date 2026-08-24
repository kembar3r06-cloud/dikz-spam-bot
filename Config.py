cat > config.py << 'EOF'
# Configuration
RATE_LIMIT_DELAY = 2  # detik antar request
TIMEOUT = 5
MAX_RETRIES = 2

# Endpoints (bisa tambah sendiri)
ACTIVE_ENDPOINTS = True
LOG_HISTORY = True
EOF
