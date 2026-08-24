cat > main.py << 'EOF'
#!/usr/bin/env python3
import os
import sys
import time
import json
import subprocess
from spam_engine import SpamEngine

class DikzSpamTermux:
    def __init__(self):
        self.spam = SpamEngine()
        self.running = True
    
    def clear_screen(self):
        os.system('clear')
    
    def banner(self):
        print("""
╔═══════════════════════════════════╗
║   DIKZ SPAM BOT - TERMUX EDITION  ║
║        King Egi 😈💥             ║
║  « Cold coffee warm I can't »     ║
╚═══════════════════════════════════╝
        """)
    
    def menu(self):
        self.clear_screen()
        self.banner()
        print("""
┌─ MAIN MENU ─────────────────────┐
│                                 │
│  1. 🔥 Mulai Spam OTP           │
│  2. 📋 Lihat History            │
│  3. ⚙️  Settings                │
│  4. ℹ️  Info                    │
│  5. ❌ Exit                     │
│                                 │
└─────────────────────────────────┘
        """)
        pilihan = input("➤ Pilih [1-5]: ").strip()
        return pilihan
    
    def spam_menu(self):
        """Main spam function"""
        self.clear_screen()
        print("╔════ SPAM OTP ════╗\n")
        
        try:
            nomor = input("📱 Nomor Target (contoh: 089508226367): ").strip()
            
            # Validasi nomor
            if not nomor.isdigit() or len(nomor) < 10:
                print("❌ Nomor invalid (min 10 digit)")
                time.sleep(2)
                return
            
            jumlah = input("📊 Jumlah Spam (default 50): ").strip() or "50"
            
            try:
                jumlah = int(jumlah)
            except ValueError:
                print("❌ Jumlah harus angka")
                time.sleep(2)
                return
            
            # Confirm
            print(f"""
╔════════════════════════════════╗
║    ⚠️  KONFIRMASI SPAM ⚠️      ║
╠════════════════════════════════╣
║  Target  : {nomor}
║  Jumlah  : {jumlah}x
╚════════════════════════════════╝
            """)
            
            konfirm = input("Lanjut? (y/n): ").strip().lower()
            if konfirm != 'y':
                print("❌ Dibatalkan")
                time.sleep(2)
                return
            
            # Execute spam
            print("\n🔥 Spam dimulai...\n")
            result = self.spam.spam_termux(nomor, jumlah, callback=self.progress)
            
            print(f"""
╔════════════════════════════════╗
║       ✓ SPAM SELESAI ✓        ║
╠════════════════════════════════╣
║  Sukses  : {result['success']} request
║  Gagal   : {result['failed']} request
║  Total   : {result['success'] + result['failed']}
╚════════════════════════════════╝
            """)
            
            time.sleep(3)
        
        except KeyboardInterrupt:
            print("\n\n❌ Dibatalkan user")
            time.sleep(2)
    
    def progress(self, msg):
        """Progress callback"""
        print(f"  {msg}")
    
    def history_menu(self):
        """Show spam history"""
        self.clear_screen()
        print("╔════ HISTORY ════╗\n")
        
        try:
            with open('logs/history.json', 'r') as f:
                history = json.load(f)
                for i, log in enumerate(history[-10:], 1):
                    print(f"{i}. {log['nomor']} - {log['jumlah']}x - {log['time']}")
        except FileNotFoundError:
            print("📭 Belum ada history")
        
        input("\nTekan Enter untuk kembali...")
    
    def settings_menu(self):
        """Settings"""
        self.clear_screen()
        print("╔════ SETTINGS ════╗\n")
        print("1. Change Rate Limit")
        print("2. Change Timeout")
        print("3. Reset All")
        print("4. Back\n")
        
        pilihan = input("➤ Pilih: ").strip()
        if pilihan == '4':
            return
        
        input("Fitur coming soon... Tekan Enter")
    
    def info_menu(self):
        """Info"""
        self.clear_screen()
        print("""
╔═══════════════════════════════════╗
║         DIKZ SPAM INFO            ║
╠═══════════════════════════════════╣
║  Version : 1.0 (Termux Edition)  ║
║  Author  : King Egi 😈💥        ║
║  Endpoint: 60+                    ║
║  Status  : Active                 ║
║                                   ║
║  ⚠️  Disclaimer:                 ║
║  Hanya untuk testing & learning   ║
║  Gunakan dengan bertanggung jawab ║
║                                   ║
║  Github: github.com/kingegi       ║
║  Telegram: @kingegi_spam          ║
╚═══════════════════════════════════╝
        """)
        input("\nTekan Enter untuk kembali...")
    
    def run(self):
        """Main loop"""
        while self.running:
            pilihan = self.menu()
            
            if pilihan == '1':
                self.spam_menu()
            elif pilihan == '2':
                self.history_menu()
            elif pilihan == '3':
                self.settings_menu()
            elif pilihan == '4':
                self.info_menu()
            elif pilihan == '5':
                self.clear_screen()
                print("👋 Terima kasih, Egi!")
                sys.exit(0)
            else:
                print("❌ Pilihan invalid")
                time.sleep(1)

if __name__ == '__main__':
    try:
        bot = DikzSpamTermux()
        bot.run()
    except KeyboardInterrupt:
        print("\n\n❌ Bot ditutup")
        sys.exit(0)
EOF
