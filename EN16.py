from re import A
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
import random
import time
from datetime import datetime
import requests
import json
import hashlib
import os
import csv

warnings.filterwarnings('ignore')

# ✅✅✅ SOLUSI 3: PASTIKAN FOLDER DATA ADA ✅✅✅
os.makedirs('data', exist_ok=True)

# ==================== KONFIGURASI & WARNA ====================
st.set_page_config(
    page_title="EasyNatorics - Jelajah Kombinatorika", 
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# FUTURISTIC COLOR PALETTE
COLORS = {
    'primary': '#00D4FF',
    'secondary': '#FF0080', 
    'accent1': '#7928CA',
    'accent2': '#FF6B35',
    'accent3': '#00F5FF',
    'dark': '#0A0A0A',
    'darker': '#111111',
    'light': '#1A1A1A',
    'text': '#FFFFFF'
}

# RGBA versions for transparency
COLORS_RGBA = {
    'primary': 'rgba(0, 212, 255, 0.3)',
    'secondary': 'rgba(255, 0, 128, 0.3)',
    'accent1': 'rgba(121, 40, 202, 0.3)',
    'accent2': 'rgba(255, 107, 53, 0.3)'
}

# ==================== CSS MODERN & UNIK DENGAN ANIMASI ====================
def apply_futuristic_style():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');
    
    * {{
        font-family: 'Exo 2', sans-serif;
    }}
    
    .stApp {{
        background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['darker']} 100%);
        color: {COLORS['text']};
    }}
    
    .main-title {{
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['accent2']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.5rem;
        margin-bottom: 2rem;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
    }}
    
    .section-header {{
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        color: {COLORS['primary']};
        font-size: 2rem;
        margin: 2rem 0 1rem 0;
        border-left: 4px solid {COLORS['secondary']};
        padding-left: 1rem;
    }}
    
    .metric-card {{
        background: linear-gradient(145deg, {COLORS['light']}, {COLORS['darker']});
        border: 1px solid {COLORS['primary']}33;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        backdrop-filter: blur(10px);
    }}
    
    .stat-value {{
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['accent2']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }}
    
    .stat-label {{
        color: {COLORS['text']};
        text-align: center;
        font-size: 1rem;
        opacity: 0.8;
    }}
    
    .improvement-badge {{
        background: linear-gradient(90deg, {COLORS['accent1']}, {COLORS['secondary']});
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem 0;
    }}
    
    .conclusion-box {{
        background: linear-gradient(135deg, {COLORS['accent1']}22, {COLORS['primary']}22);
        border: 1px solid {COLORS['primary']}44;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border-left: 5px solid {COLORS['secondary']};
    }}
    
    .research-card {{
        background: linear-gradient(145deg, {COLORS['light']}, {COLORS['darker']});
        border: 1px solid {COLORS['primary']}33;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        animation: cardSlideIn 0.6s ease-out;
    }}
    
    @keyframes cardSlideIn {{
        from {{ 
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{ 
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .research-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,212,255,0.2);
    }}
    
    .test-card {{
        background: linear-gradient(135deg, {COLORS['secondary']} 0%, {COLORS['accent2']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(255, 0, 128, 0.3);
        animation: pulseGlow 2s infinite;
        border: 2px solid rgba(255,255,255,0.3);
    }}
    
    @keyframes pulseGlow {{
        0%, 100% {{ box-shadow: 0 8px 25px rgba(255, 0, 128, 0.3); }}
        50% {{ box-shadow: 0 8px 30px rgba(255, 0, 128, 0.6); }}
    }}
    
    .problem-card {{
        background: linear-gradient(135deg, {COLORS['accent1']} 0%, {COLORS['primary']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(121, 40, 202, 0.3);
        transition: all 0.3s ease;
        animation: problemCardEntrance 0.8s ease-out;
    }}
    
    @keyframes problemCardEntrance {{
        from {{ 
            opacity: 0;
            transform: scale(0.9) translateX(-20px);
        }}
        to {{ 
            opacity: 1;
            transform: scale(1) translateX(0);
        }}
    }}
    
    .learning-card {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent3']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
        animation: learningCardFloat 3s ease-in-out infinite;
    }}
    
    @keyframes learningCardFloat {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-3px); }}
    }}
    
    .success-card {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent3']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 3px solid {COLORS['accent2']};
        animation: successCelebrate 0.6s ease-out, pulse 2s infinite 0.6s;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
    }}
    
    @keyframes successCelebrate {{
        0% {{ transform: scale(0.8); opacity: 0; }}
        70% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}
    
    .explanation-box {{
        background: linear-gradient(135deg, {COLORS['light']} 0%, {COLORS['darker']} 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 5px solid {COLORS['primary']};
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        animation: explanationReveal 0.8s ease-out;
    }}
    
    @keyframes explanationReveal {{
        from {{ 
            opacity: 0;
            transform: translateX(-20px);
            max-height: 0;
        }}
        to {{ 
            opacity: 1;
            transform: translateX(0);
            max-height: 500px;
        }}
    }}
    
    .testimonial-card {{
        background: linear-gradient(135deg, {COLORS['accent1']} 0%, {COLORS['secondary']} 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(121, 40, 202, 0.3);
        animation: testimonialSlide 0.6s ease-out;
        transition: all 0.3s ease;
    }}
    
    @keyframes testimonialSlide {{
        from {{ 
            opacity: 0;
            transform: translateX(30px);
        }}
        to {{ 
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    .anxiety-improvement-card {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent3']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 3px solid {COLORS['accent2']};
        text-align: center;
        animation: improvementGlow 3s infinite;
    }}
    
    @keyframes improvementGlow {{
        0%, 100% {{ box-shadow: 0 0 20px rgba(0, 212, 255, 0.3); }}
        50% {{ box-shadow: 0 0 30px rgba(0, 212, 255, 0.6); }}
    }}
    
    .confetti {{
        position: fixed;
        width: 10px;
        height: 10px;
        background: {COLORS['accent2']};
        animation: confettiFall 5s linear forwards;
        z-index: 1000;
    }}
    
    @keyframes confettiFall {{
        0% {{
            transform: translateY(-100px) rotate(0deg);
            opacity: 1;
        }}
        100% {{
            transform: translateY(1000px) rotate(360deg);
            opacity: 0;
        }}
    }}
    
    .floating-emoji {{
        animation: floatAround 6s ease-in-out infinite;
        display: inline-block;
        font-size: 2rem;
    }}
    
    @keyframes floatAround {{
        0%, 100% {{ 
            transform: translate(0, 0) rotate(0deg); 
        }}
        25% {{ 
            transform: translate(10px, -15px) rotate(5deg); 
        }}
        50% {{ 
            transform: translate(-5px, -25px) rotate(-5deg); 
        }}
        75% {{ 
            transform: translate(-10px, -15px) rotate(3deg); 
        }}
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}
    
    .stButton button {{
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, {COLORS['primary']}, {COLORS['accent1']});
        color: white;
    }}
    
    .stButton button:hover {{
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 212, 255, 0.3);
    }}
    
    .continue-button {{
        background: linear-gradient(135deg, {COLORS['secondary']}, {COLORS['accent2']});
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 20px 0;
        display: block;
        width: 100%;
        text-align: center;
    }}
    
    .continue-button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(255, 0, 128, 0.4);
    }}
    </style>
    """, unsafe_allow_html=True)

# ==================== UTILITY FUNCTIONS ====================
def hash_answer(answer):
    """Hash answer for secure comparison"""
    return hashlib.sha256(str(answer).encode()).hexdigest()

def validate_demographics(demographics):
    """Validate participant demographics"""
    errors = []
    
    if not demographics.get('nama') or len(demographics['nama'].strip()) < 2:
        errors.append("Nama harus minimal 2 karakter")
    
    if not demographics.get('kelas'):
        errors.append("Kelas harus dipilih")
    
    if not demographics.get('usia') or demographics['usia'] not in range(15, 19):
        errors.append("Usia harus antara 15-18 tahun")
    
    if not demographics.get('pengalaman'):
        errors.append("Pengalaman matematika harus dipilih")
    
    return errors

def create_confetti():
    """Create confetti effect"""
    confetti_html = """
    <div id="confetti-container" style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:1000;">
    """
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent1'], COLORS['accent2'], COLORS['accent3']]
    for i in range(50):
        color = random.choice(colors)
        size = random.randint(8, 15)
        left = random.randint(0, 100)
        delay = random.uniform(0, 2)
        duration = random.uniform(3, 6)
        confetti_html += f"""
        <div class="confetti" style="
            background: {color};
            width: {size}px;
            height: {size}px;
            left: {left}%;
            animation-delay: {delay}s;
            animation-duration: {duration}s;
        "></div>
        """
    confetti_html += "</div>"
    return confetti_html

def show_celebration():
    """Show celebration effects"""
    # Confetti
    st.markdown(create_confetti(), unsafe_allow_html=True)
    
    # Floating emojis
    emojis = ["🎉", "🎊", "🌟", "🚀", "💫", "🔥", "⭐", "✨"]
    emoji_html = "<div style='text-align: center; margin: 2rem 0;'>"
    for emoji in random.sample(emojis, 4):
        emoji_html += f"<span class='floating-emoji' style='animation-delay: {random.uniform(0, 2)}s;'>{emoji}</span> "
    emoji_html += "</div>"
    st.markdown(emoji_html, unsafe_allow_html=True)

# ==================== AI LAYER - DEEPSEEK INTEGRATION ====================
class DeepSeekAI:
    def __init__(self):
        self.api_key = st.secrets["DEEPSEEK_API_KEY"]
        self.demo_mode = False 
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
        self.demo_mode = self.api_key == "sk-cf4ef9db521343d085ad9e4992876720"
    
    def get_ai_explanation(self, concept, student_level, previous_answers=None):
        """Dapatkan penjelasan AI yang personalized dari DeepSeek"""
        
        if self.demo_mode:
            # Fallback explanations for demo mode
            explanations = {
                "prinsip_perkalian": """
                **🎯 PRINSIP PERKALIAN - Seni Menghitung Kemungkinan**
                
                **Konsep Inti:** 
                "Jika ada n₁ cara melakukan hal pertama, n₂ cara melakukan hal kedua, ..., nₖ cara melakukan hal ke-k, 
                maka total cara melakukan semua hal tersebut adalah n₁ × n₂ × ... × nₖ"
                
                **🧠 Analogi Mendalam:**
                Bayangkan kamu menjadi **event organizer** pesta!
                - **Makanan**: 4 pilihan (Ayam, Ikan, Sapi, Vegetarian)
                - **Minuman**: 3 pilihan (Jus, Soda, Teh)  
                - **Dessert**: 2 pilihan (Ice Cream, Pudding)
                
                Total paket pesta = 4 × 3 × 2 = **24 kombinasi unik!**
                
                **📊 Contoh Real-World:**
                1. **Password 3 digit**: 10 × 10 × 10 = 1,000 kombinasi
                2. **Rute perjalanan**: 3 bus × 2 kereta × 4 pesawat = 24 rute
                3. **Menu restoran**: 5 appetizer × 8 main × 3 dessert = 120 menu
                
                **🎯 Kapan Digunakan?**
                - Semua pilihan **INDEPENDEN** (pilihan pertama tidak mempengaruhi pilihan kedua)
                - Urutan pilihan **TIDAK PENTING** dalam proses
                - Setiap kombinasi menghasilkan hasil yang berbeda
                """,
                
                "permutasi": """
                **🔄 PERMUTASI - Seni Menyusun dengan Presisi**
                
                **Konsep Inti:**
                "Banyaknya cara menyusun r objek dari n objek berbeda dimana **URUTAN PENTING**"
                
                **Formula Sakti:** 
                P(n,r) = n! / (n-r)!   atau   nPr = n × (n-1) × ... × (n-r+1)
                
                **🎭 Analogi Mendalam:**
                Bayangkan menjadi **sutradara film** yang menyusun adegan!
                - Ada 5 aktor: Andi, Budi, Cici, Dedi, Eka
                - Hanya 3 yang bisa tampil dalam satu adegan
                - Setiap urutan aktor = adegan yang berbeda!
                
                Total susunan = P(5,3) = 5 × 4 × 3 = **60 adegan unik!**
                
                **📊 Contoh Real-World:**
                1. **Podium lomba**: 8 peserta → 8! = 40,320 urutan juara
                2. **Password unik**: 4 karakter berbeda → P(26,4) = 358,800 password
                3. **Susunan delegasi**: 6 orang di meja → (6-1)! = 120 susunan
                
                **🎯 Kapan Digunakan?**
                - **URUTAN PENTING** (A-B-C ≠ C-B-A)
                - Posisi/ranking menentukan hasil
                - Setiap "tempat" harus diisi oleh objek berbeda
                """,
                
                "kombinasi": """
                **👥 KOMBINASI - Power of Team Selection**
                
                **Konsep Inti:**
                "Banyaknya cara memilih r objek dari n objek berbeda dimana **URUTAN TIDAK PENTING**"
                
                **Formula Sakti:**
                C(n,r) = n! / (r! × (n-r)!)   atau   nCr = P(n,r) / r!
                
                **🤝 Analogi Mendalam:**
                Bayangkan menjadi **manajer tim** yang memilih pemain!
                - Ada 7 pemain cadangan: A, B, C, D, E, F, G
                - Perlu memilih 3 untuk starting lineup
                - Tim A-B-C = C-B-A → urutan tidak penting!
                
                Total tim = C(7,3) = 35 tim berbeda!
                
                **📊 Contoh Real-World:**
                1. **Komite**: Pilih 4 dari 10 orang → C(10,4) = 210 komite
                2. **Menu combo**: Pilih 3 side dish dari 8 → C(8,3) = 56 combo
                3. **Sampling QC**: Pilih 5 produk dari 100 → C(100,5) kombinasi
                
                **🎯 Kapan Digunakan?**
                - **URUTAN TIDAK PENTING** (A-B-C = C-B-A)
                - Hanya anggota/set yang penting
                - Seleksi, pemilihan, pembentukan grup
                """
            }
            return explanations.get(concept, "Penjelasan lengkap akan tersedia.")
        
        else:
            # Real DeepSeek API call
            try:
                prompt = f"""
                Berikan penjelasan tentang {concept} dalam kombinatorika untuk siswa SMA level {student_level}.
                Buat penjelasan yang:
                1. Mudah dipahami dengan analogi sehari-hari
                2. Menyertakan contoh konkret
                3. Menjelaskan kapan konsep ini digunakan
                4. Berikan tips mengerjakan soal
                5. Gunakan format Markdown dengan emoji
                6. Maksimal 500 kata
                """
                
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": "Anda adalah tutor matematika yang ahli dalam kombinatorika dan pedagogi. Jelaskan dengan cara yang mudah dipahami siswa SMA."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                }
                
                response = requests.post(self.base_url, headers=headers, json=data, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    return result['choices'][0]['message']['content']
                else:
                    # If API fails, provide basic explanation
                    basic_explanations = {
                        "prinsip_perkalian": "**Prinsip Perkalian**: Jika ada n₁ cara melakukan hal pertama, n₂ cara melakukan hal kedua, maka total cara = n₁ × n₂ × ...",
                        "permutasi": "**Permutasi**: Menyusun objek dengan memperhatikan URUTAN. Rumus: P(n,r) = n!/(n-r)!",
                        "kombinasi": "**Kombinasi**: Memilih objek TANPA memperhatikan urutan. Rumus: C(n,r) = n!/(r!(n-r)!)"
                    }
                    return basic_explanations.get(concept, "Konsep ini akan dijelaskan lebih detail.")
                    
            except Exception as e:
                return f"Koneksi AI sedang gangguan. Error: {str(e)}"

    def get_personalized_feedback(self, question, student_answer, correct_answer, concept):
        """Dapatkan feedback personalized dari DeepSeek AI"""
        
        if self.demo_mode:
            motivational_phrases = [
                "Kamu seperti detektif matematika yang sedang memecahkan misteri! 🔍",
                "Setiap langkah membawamu lebih dekat ke pemahaman yang mendalam! 💪", 
                "Pikiranmu sedang membangun jalur neural yang kuat! 🧠",
                "Seperti puzzle, setiap bagian akan membentuk gambaran yang sempurna! 🧩",
                "Kamu sedang menanam benih pengetahuan yang akan tumbuh subur! 🌱"
            ]
            
            if student_answer == correct_answer:
                return f"**🎉 LUAR BIASA! Jawaban TEPAT!**\n\nKamu benar-benar menguasai {concept}! {random.choice(motivational_phrases)}"
            else:
                return f"**💪 ALMOST THERE!**\n\nSedikit lagi menguasai {concept}! {random.choice(motivational_phrases)}"
        
        else:
            try:
                prompt = f"""
                Berikan feedback untuk siswa yang mengerjakan soal kombinatorika:
                
                Soal: {question}
                Jawaban siswa: {student_answer}
                Jawaban benar: {correct_answer}
                Konsep: {concept}
                
                Berikan feedback yang:
                1. Motivational dan supportive
                2. Jelaskan kesalahan jika ada (jika jawaban salah)
                3. Berikan petunjuk untuk perbaikan
                4. Gunakan bahasa yang friendly dengan emoji
                5. Maksimal 3 kalimat
                """
                
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": "Anda adalah tutor matematika yang supportive dan memahami."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 300
                }
                
                response = requests.post(self.base_url, headers=headers, json=data, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    return result['choices'][0]['message']['content']
                else:
                    return "Feedback AI sementara tidak tersedia."
                    
            except Exception as e:
                return "Koneksi feedback AI sedang gangguan."

    def ask_ai_tutor(self, user_question, context=""):
        """Fungsi untuk chat dengan AI tutor"""
        if self.demo_mode:
            # Berikan jawaban yang lebih helpful di demo mode
            demo_responses = {
                "prinsip perkalian": """
                **Prinsip Perkalian** 🧮 
                
                Analogi: Jika ada 3 cara memilih baju dan 4 cara memilih celana, maka total kombinasi = 3 × 4 = **12 outfit**!
                
                **Contoh:**
                - Menu: 4 makanan × 3 minuman × 2 dessert = 24 kombinasi
                - Password: 10 angka × 10 angka × 10 angka = 1000 kombinasi
                
                **Rumus:** n₁ × n₂ × n₃ × ...
                """,
                
                "permutasi": """
                **Permutasi** 🔄
                
                Analogi: Menyusun 3 buku dari 5 buku berbeda = 5 × 4 × 3 = **60 susunan** (urutan penting!)
                
                **Contoh:**
                - Podium juara: 8 peserta → P(8,3) = 336 susunan
                - Password unik: 4 huruf berbeda → P(26,4) = 358.800
                
                **Rumus:** P(n,r) = n! / (n-r)!
                """, 
                
                "kombinasi": """
                **Kombinasi** 👥
                
                Analogi: Memilih 2 orang dari 5 orang = **10 tim** (urutan tidak penting!)
                
                **Contoh:**
                - Komite: Pilih 4 dari 10 → C(10,4) = 210 komite
                - Menu combo: Pilih 2 dari 6 hidangan → C(6,2) = 15 combo
                
                **Rumus:** C(n,r) = n! / (r!(n-r)!)
                """
            }
            
            # Cek jika pertanyaan tentang topik tertentu
            question_lower = user_question.lower()
            for topic, response in demo_responses.items():
                if topic in question_lower:
                    return f"🤖 **AI Tutor (Demo Mode):**\n\n{response}"
            
            return "🤖 **AI Tutor (Demo Mode):**\n\nFitur AI Tutor lengkap tersedia dengan API key DeepSeek yang valid. Untuk sekarang, Anda bisa bertanya tentang:\n\n• **Prinsip Perkalian** 🧮\n• **Permutasi** 🔄  \n• **Kombinasi** 👥\n\nSilakan tanyakan salah satu topik di atas!"
        
        else:
            try:
                prompt = f"""
                Anda adalah AI Tutor matematika untuk siswa SMA yang belajar kombinatorika.
                
                KONTEKS MATERI: {context}
                PERTANYAAN SISWA: {user_question}
                
                Tolong berikan penjelasan yang:
                - Mudah dipahami siswa SMA
                - Gunakan analogi sehari-hari
                - Berikan contoh konkret
                - Sertakan langkah-langkah sederhana
                - Format dengan markdown dan emoji
                - Maksimal 300 kata
                - Bahasa Indonesia yang friendly dan suportif
                """
                
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": "deepseek-chat",
                    "messages": [
                        {
                            "role": "system", 
                            "content": "Anda adalah tutor matematika yang sabar, ramah, dan ahli menjelaskan konsep sulit dengan cara mudah. Gunakan bahasa Indonesia yang friendly untuk siswa SMA. Berikan contoh konkret dan analogi sehari-hari."
                        },
                        {
                            "role": "user", 
                            "content": prompt
                        }
                    ],
                    "temperature": 0.7,
                    "max_tokens": 800
                }
                
                response = requests.post(self.base_url, headers=headers, json=data, timeout=20)
                
                if response.status_code == 200:
                    result = response.json()
                    return f"🤖 **AI Tutor:**\n\n{result['choices'][0]['message']['content']}"
                elif response.status_code == 401:
                    return "🔑 **Error:** API Key tidak valid. Pastikan Anda menggunakan DeepSeek API key yang benar."
                elif response.status_code == 429:
                    return "⏳ **Error:** Terlalu banyak permintaan. Silakan coba lagi dalam beberapa menit."
                else:
                    return f"🤖 **Error:** AI Tutor sedang mengalami gangguan (Error {response.status_code}). Silakan coba lagi nati."
                    
            except requests.exceptions.Timeout:
                return "⏰ **Error:** Waktu permintaan habis. Pastikan koneksi internet stabil."
            except requests.exceptions.ConnectionError:
                return "🌐 **Error:** Koneksi internet terputus. Periksa koneksi Anda."
            except Exception as e:
                return "🤖 **Error:** Terjadi kesalahan sistem. Silakan refresh halaman dan coba lagi."
# ==================== DATA PERSISTENCE LAYER ====================
class DataExporter:
    @staticmethod
    def export_participant_data(participant_data):
        """Export single participant data to CSV"""
        try:
            participant_id = participant_data.get('participant_id', 'unknown')
            
            # Buat nama file yang aman
            safe_name = participant_data['demographics'].get('nama', 'unknown').replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"data/participant_{safe_name}_{timestamp}.csv"
            
            # Calculate time spent
            start_time = participant_data.get('registration_time')
            end_time = datetime.now().isoformat()
            
            if start_time:
                try:
                    start_dt = datetime.fromisoformat(start_time)
                    end_dt = datetime.fromisoformat(end_time)
                    time_spent_minutes = (end_dt - start_dt).total_seconds() / 60
                except:
                    time_spent_minutes = 0
            else:
                time_spent_minutes = 0
            
            # Prepare data dengan error handling
            pre_test_score = participant_data['pre_test'].get('score', 0)
            post_test_score = participant_data['post_test'].get('score', 0)
            pre_anxiety = participant_data['anxiety_survey'].get('pre_score', 0)
            post_anxiety = participant_data['anxiety_survey'].get('post_score', 0)
            
            # Handle None values
            pre_test_score = pre_test_score if pre_test_score is not None else 0
            post_test_score = post_test_score if post_test_score is not None else 0
            pre_anxiety = pre_anxiety if pre_anxiety is not None else 0
            post_anxiety = post_anxiety if post_anxiety is not None else 0
            
            problems_attempted = participant_data['learning_progress'].get('problems_attempted', 0)
            problems_correct = participant_data['learning_progress'].get('problems_correct', 0)
            
            if problems_attempted > 0:
                accuracy_rate = (problems_correct / problems_attempted) * 100
            else:
                accuracy_rate = 0
            
            data = {
                'participant_id': participant_id,
                'nama': participant_data['demographics'].get('nama', ''),
                'kelas': participant_data['demographics'].get('kelas', ''),
                'usia': participant_data['demographics'].get('usia', ''),
                'pengalaman_matematika': participant_data['demographics'].get('pengalaman', ''),
                'pre_anxiety_score': pre_anxiety,
                'post_anxiety_score': post_anxiety,
                'anxiety_reduction': pre_anxiety - post_anxiety,
                'pre_test_score': pre_test_score,
                'post_test_score': post_test_score,
                'learning_gain': post_test_score - pre_test_score,
                'problems_attempted': problems_attempted,
                'problems_correct': problems_correct,
                'accuracy_rate': accuracy_rate,
                'concepts_learned': ', '.join(participant_data['learning_progress'].get('concepts_learned', [])),
                'time_spent_minutes': round(time_spent_minutes, 2),
                'testimonial': participant_data['satisfaction_survey'].get('testimonial', ''),
                'completion_date': end_time
            }
            
            # Ensure data directory exists
            os.makedirs('data', exist_ok=True)
            
            # Write to CSV
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
            
            return filename
        
        except Exception as e:
            st.error(f"❌ Error exporting data: {str(e)}")
            return None

    @staticmethod
    def export_all_research_data():
        """Export all research data to CSV"""
        try:
            research_data = st.session_state.research_data
            participants = research_data.get('participants', {})
            
            if not participants:
                st.warning("📊 Tidak ada data peserta untuk diexport")
                return None
            
            all_data = []
            for participant_id, participant_data in participants.items():
                # Reuse the single participant export logic
                filename = DataExporter.export_participant_data(participant_data)
                if filename:
                    all_data.append(participant_data)
            
            if all_data:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                summary_filename = f"data/research_summary_{timestamp}.csv"
                
                # Create summary file
                if all_data:
                    # Use the first participant's data structure
                    sample_data = DataExporter.export_participant_data(all_data[0])
                    if sample_data:
                        st.success(f"✅ Semua data berhasil diexport! Total: {len(all_data)} peserta")
                        return summary_filename
            
            return None
            
        except Exception as e:
            st.error(f"❌ Error exporting research data: {str(e)}")
            return None

# ==================== SISTEM DATA PENELITIAN ====================
class ResearchDataSystem:
    def __init__(self):
        if 'research_data' not in st.session_state:
            st.session_state.research_data = {
                'participants': {},
                'current_participant': None,
                'study_start_time': datetime.now().isoformat()
            }
        
        if 'participant_data' not in st.session_state:
            st.session_state.participant_data = self._create_new_participant()
            
        if 'current_module' not in st.session_state:
            st.session_state.current_module = None

    def _create_new_participant(self):
        """Create a new participant template"""
        return {
            'participant_id': None,
            'demographics': {},
            'pre_test': {
                'score': None,
                'answers': [],
                'start_time': None,
                'completion_time': None
            },
            'post_test': {
                'score': None, 
                'answers': [],
                'start_time': None,
                'completion_time': None
            },
            'anxiety_survey': {
                'pre_score': None,
                'post_score': None,
                'amas_score': None,
                'responses': []
            },
            'satisfaction_survey': {
                'score': None,
                'responses': [],
                'testimonial': ''
            },
            'learning_progress': {
                'concepts_learned': [],
                'problems_attempted': 0,
                'problems_correct': 0,
                'total_time': 0,
                'current_module': 0,
                'module_progress': {
                    'prinsip_perkalian': {'completed': False, 'score': 0},
                    'permutasi': {'completed': False, 'score': 0},
                    'kombinasi': {'completed': False, 'score': 0}
                }
            },
            'completion_status': {
                'diagnostic_done': False,
                'foundational_done': False,
                'application_done': False,
                'improvement_done': False,
                'post_assessment_done': False
            },
            'registration_time': datetime.now().isoformat()
        }

    def register_participant(self, demographics):
        """Register new participant with validation"""
        try:
            # Validate demographics
            errors = validate_demographics(demographics)
            if errors:
                raise ValueError("; ".join(errors))
            
            # Generate participant ID
            participant_id = f"P{len(st.session_state.research_data['participants']) + 1:03d}"
            
            # Create new participant
            new_participant = self._create_new_participant()
            new_participant['participant_id'] = participant_id
            new_participant['demographics'] = demographics
            new_participant['pre_test']['start_time'] = datetime.now().isoformat()
            
            # Store in session state
            st.session_state.participant_data = new_participant
            st.session_state.research_data['participants'][participant_id] = new_participant
            st.session_state.research_data['current_participant'] = participant_id
            
            return participant_id
        
        except ValueError as e:
            st.error(f"❌ Validasi gagal: {e}")
            return None
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
            return None

    def calculate_amas_score(self, responses):
        """Hitung skor AMAS berdasarkan respon (skala 1-5)"""
        if not responses:
            return None
        try:
            return np.mean([r['response'] for r in responses])
        except:
            return None

    def get_anxiety_level(self, amas_score):
        """Kategorikan tingkat kecemasan berdasarkan skor AMAS"""
        if amas_score is None:
            return "Tidak Terukur"
        elif amas_score <= 2.0:
            return "Rendah"
        elif amas_score <= 3.5:
            return "Sedang"
        else:
            return "Tinggi"

    def update_learning_progress(self, concept, is_correct=False):
        """Update learning progress when student answers a question"""
        try:
            current_id = st.session_state.research_data['current_participant']
            if current_id:
                participant = st.session_state.research_data['participants'][current_id]
                
                # Track attempt
                participant['learning_progress']['problems_attempted'] += 1
                
                # Track correctness
                if is_correct:
                    participant['learning_progress']['problems_correct'] += 1
                
                # Track concept learned
                if concept not in participant['learning_progress']['concepts_learned']:
                    participant['learning_progress']['concepts_learned'].append(concept)
                
                return True
        except Exception as e:
            st.error(f"Error updating progress: {e}")
        return False

    def complete_module(self, module_key):
        """Mark a module as completed"""
        try:
            current_id = st.session_state.research_data['current_participant']
            if current_id:
                participant = st.session_state.research_data['participants'][current_id]
                participant['learning_progress']['module_progress'][module_key]['completed'] = True
                return True
        except Exception as e:
            st.error(f"Error completing module: {e}")
        return False

# ==================== INSTRUMEN PENELITIAN - AMAS ====================
class ResearchInstruments:
    def __init__(self):
        # AMAS (Abbreviated Math Anxiety Scale) - 9 items
        self.amas_questions = [
            {
                "question": "Mengerjakan soal matematika yang diberikan guru",
                "category": "Learning Mathematics"
            },
            {
                "question": "Mengerjakan soal matematika di papan tulis", 
                "category": "Learning Mathematics"
            },
            {
                "question": "Mengerjakan ujian matematika",
                "category": "Evaluation Mathematics"
            },
            {
                "question": "Mempersiapkan ujian matematika",
                "category": "Evaluation Mathematics"
            },
            {
                "question": "Mendengar pelajaran matematika",
                "category": "Learning Mathematics"
            },
            {
                "question": "Mengerjakan PR matematika",
                "category": "Learning Mathematics"
            },
            {
                "question": "Membaca soal matematika di buku",
                "category": "Learning Mathematics"
            },
            {
                "question": "Mendapat nilai matematika yang buruk",
                "category": "Evaluation Mathematics"
            },
            {
                "question": "Memikirkan pelajaran matematika besok",
                "category": "Evaluation Mathematics"
            }
        ]
        
        # Pre Test Questions (Different from Post Test)
        self.pre_test_questions = [
            {
                "id": 1,
                "question": "Sebuah restoran menawarkan 4 jenis makanan utama, 3 jenis minuman, dan 2 jenis dessert. Berapa banyak kombinasi menu yang berbeda yang dapat dipilih pelanggan?",
                "options": ["9", "12", "24", "36"],
                "correct_answer": "24",
                "concept": "prinsip_perkalian",
                "explanation": "Menggunakan prinsip perkalian: 4 makanan × 3 minuman × 2 dessert = 24 kombinasi"
            },
            {
                "id": 2,
                "question": "Dalam lomba lari 100m, ada 8 peserta. Berapa banyak kemungkinan susunan juara 1, 2, dan 3?",
                "options": ["56", "336", "512", "40320"],
                "correct_answer": "336",
                "concept": "permutasi",
                "explanation": "Menggunakan permutasi P(8,3) = 8 × 7 × 6 = 336 susunan"
            },
            {
                "id": 3,
                "question": "Dari 10 orang, akan dipilih 4 orang untuk menjadi panitia. Berapa banyak cara memilih panitia tersebut?",
                "options": ["40", "210", "5040", "10000"],
                "correct_answer": "210",
                "concept": "kombinasi",
                "explanation": "Menggunakan kombinasi C(10,4) = 10!/(4!×6!) = 210 cara"
            },
            {
                "id": 4,
                "question": "Berapa banyak kata 4 huruf yang dapat disusun dari huruf-huruf pada kata 'MAJU'?",
                "options": ["16", "24", "256", "12"],
                "correct_answer": "24",
                "concept": "permutasi",
                "explanation": "Menyusun 4 huruf berbeda: 4! = 4 × 3 × 2 × 1 = 24 kata"
            },
            {
                "id": 5,
                "question": "Sebuah tim bola basket terdiri dari 5 pemain. Jika ada 12 pemain yang tersedia, berapa banyak tim berbeda yang dapat dibentuk?",
                "options": ["60", "792", "95040", "248832"],
                "correct_answer": "792",
                "concept": "kombinasi",
                "explanation": "Menggunakan kombinasi C(12,5) = 12!/(5!×7!) = 792 tim"
            }
        ]
        
        # Post Test Questions (Different from Pre Test)
        self.post_test_questions = [
            {
                "id": 1,
                "question": "Sebuah kode akses terdiri dari 2 huruf vokal (A,I,U,E,O) diikuti 3 angka. Berapa banyak kode yang mungkin?",
                "options": ["1250", "2500", "5000", "10000"],
                "correct_answer": "1250",
                "concept": "prinsip_perkalian",
                "explanation": "5 huruf vokal × 5 huruf vokal × 10 angka × 10 angka × 10 angka = 2500"
            },
            {
                "id": 2,
                "question": "Dalam suatu pertemuan, 7 orang akan duduk melingkar. Berapa banyak susunan duduk yang mungkin?",
                "options": ["5040", "720", "120", "2520"],
                "correct_answer": "720",
                "concept": "permutasi",
                "explanation": "Permutasi siklik: (7-1)! = 6! = 720 susunan"
            },
            {
                "id": 3,
                "question": "Dari 8 buku berbeda, akan dipilih 3 buku untuk dibaca. Berapa banyak pilihan yang mungkin?",
                "options": ["56", "336", "24", "512"],
                "correct_answer": "56",
                "concept": "kombinasi",
                "explanation": "C(8,3) = 8!/(3!×5!) = 56 pilihan"
            },
            {
                "id": 4,
                "question": "Berapa banyak bilangan 3 digit yang dapat dibentuk dari angka 1,2,3,4,5 tanpa pengulangan?",
                "options": ["60", "125", "15", "243"],
                "correct_answer": "60",
                "concept": "permutasi",
                "explanation": "P(5,3) = 5 × 4 × 3 = 60 bilangan"
            },
            {
                "id": 5,
                "question": "Dalam sebuah komite yang terdiri dari 5 orang, dipilih 2 orang sebagai ketua dan wakil. Berapa banyak pasangan yang mungkin?",
                "options": ["10", "20", "25", "120"],
                "correct_answer": "20",
                "concept": "permutasi",
                "explanation": "P(5,2) = 5 × 4 = 20 pasangan"
            }
        ]

    def render_amas_survey(self, survey_type="pre"):
        """Render AMAS anxiety survey"""
        st.markdown(f"""
        <div class='research-card'>
            <h2>📊 Survey Kecemasan Matematika ({'Awal' if survey_type == 'pre' else 'Akhir'})</h2>
            <p>Sebelum memulai, mari ukur tingkat kecemasan matematika Anda. Pilih seberapa cemas Anda merasa pada situasi berikut:</p>
        </div>
        """, unsafe_allow_html=True)
        
        responses = []
        participant_id = st.session_state.participant_data.get('participant_id', 'unknown')
        
        for i, item in enumerate(self.amas_questions, 1):
            st.markdown(f"**{i}. {item['question']}**")
            st.caption(f"Kategori: {item['category']}")
            
            unique_key = f"{participant_id}_amas_{survey_type}_{i}"
            
            response = st.radio(
                f"Seberapa cemas Anda?",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: {
                    1: "Tidak Cemas", 
                    2: "Sedikit Cemas", 
                    3: "Cukup Cemas", 
                    4: "Cemas", 
                    5: "Sangat Cemas"
                }[x],
                key=unique_key,
                horizontal=True
            )
            
            responses.append({
                "question": item['question'],
                "category": item['category'],
                "response": response
            })
        
        return responses

    def render_test(self, test_type="pre"):
        """Render pre/post test with different questions"""
        st.markdown(f"""
        <div class='test-card'>
            <h2>🎯 {'Diagnosis Awal' if test_type == 'pre' else 'Evaluasi Akhir'}</h2>
            <p>Jawablah soal-soal berikut untuk mengukur pemahaman Anda tentang kombinatorika:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Select the appropriate question set
        questions = self.pre_test_questions if test_type == "pre" else self.post_test_questions
        
        answers = []
        score = 0
        participant_id = st.session_state.participant_data.get('participant_id', 'unknown')
        
        for i, question in enumerate(questions, 1):
            st.markdown(f"### Soal {i}")
            st.markdown(f"**{question['question']}**")
            
            unique_key = f"{participant_id}_{test_type}_q{i}"
            
            user_answer = st.radio(
                "Pilih jawaban:",
                options=question['options'],
                key=unique_key
            )
            
            is_correct = (user_answer == question['correct_answer'])
            if is_correct:
                score += 1
            
            answers.append({
                "question_id": question['id'],
                "user_answer": user_answer,
                "correct_answer": question['correct_answer'],
                "is_correct": is_correct,
                "concept": question['concept']
            })
        
        return answers, score

# ==================== MODUL PEMBELAJARAN ====================
class LearningModules:
    def __init__(self):
        self.modules = {
            'prinsip_perkalian': {
                'title': '🔢 Prinsip Perkalian',
                'description': 'Seni Menghitung Kemungkinan',
                'level': 'Dasar',
                'problems': self._get_multiplication_problems(),
                'color': COLORS['secondary']
            },
            'permutasi': {
                'title': '🔄 Permutasi', 
                'description': 'Seni Menyusun dengan Presisi',
                'level': 'Menengah',
                'problems': self._get_permutation_problems(),
                'color': COLORS['primary']
            },
            'kombinasi': {
                'title': '👥 Kombinasi',
                'description': 'Power of Team Selection', 
                'level': 'Lanjutan',
                'problems': self._get_combination_problems(),
                'color': COLORS['accent1']
            }
        }
    
    def _get_multiplication_problems(self):
        return [
            {
                "id": "mult_1",
                "question": "Anda memiliki 3 kemeja dan 4 celana. Berapa banyak kombinasi pakaian yang dapat dibuat?",
                "answer": "12",
                "explanation": "Prinsip perkalian: 3 kemeja × 4 celana = 12 kombinasi",
                "hint": "Setiap kemeja dapat dipasangkan dengan setiap celana"
            },
            {
                "id": "mult_2", 
                "question": "Sebuah password terdiri dari 2 huruf diikuti 3 angka. Berapa banyak password yang mungkin?",
                "answer": "676000",
                "explanation": "26 huruf × 26 huruf × 10 angka × 10 angka × 10 angka = 676,000 password",
                "hint": "Huruf: 26 pilihan, Angka: 10 pilihan (0-9)"
            },
            {
                "id": "mult_3",
                "question": "Dari kota A ke B ada 3 jalan, dari B ke C ada 2 jalan. Berapa banyak rute dari A ke C melalui B?",
                "answer": "6", 
                "explanation": "3 jalan A→B × 2 jalan B→C = 6 rute total",
                "hint": "Setiap jalan A→B dapat dipasangkan dengan setiap jalan B→C"
            }
        ]
    
    def _get_permutation_problems(self):
        return [
            {
                "id": "perm_1",
                "question": "Berapa banyak cara menyusun 4 buku berbeda di rak?",
                "answer": "24",
                "explanation": "4! = 4 × 3 × 2 × 1 = 24 susunan",
                "hint": "Ini adalah permutasi dari 4 objek berbeda"
            },
            {
                "id": "perm_2",
                "question": "Dalam lomba dengan 6 peserta, berapa banyak kemungkinan juara 1, 2, dan 3?",
                "answer": "120",
                "explanation": "P(6,3) = 6 × 5 × 4 = 120 kemungkinan",
                "hint": "Permutasi 3 dari 6 objek"
            },
            {
                "id": "perm_3",
                "question": "Berapa banyak kata 3 huruf dari huruf A, B, C, D (tidak berulang)?",
                "answer": "24",
                "explanation": "P(4,3) = 4 × 3 × 2 = 24 kata",
                "hint": "Setiap posisi huruf memiliki pilihan yang berkurang"
            }
        ]
    
    def _get_combination_problems(self):
        return [
            {
                "id": "comb_1",
                "question": "Dari 8 orang, berapa banyak cara memilih 3 orang untuk panitia?",
                "answer": "56",
                "explanation": "C(8,3) = 8!/(3!×5!) = 56 cara",
                "hint": "Urutan pemilihan tidak penting"
            },
            {
                "id": "comb_2",
                "question": "Dalam menu ada 6 hidangan. Berapa banyak cara memilih 2 hidangan?",
                "answer": "15", 
                "explanation": "C(6,2) = 6!/(2!×4!) = 15 cara",
                "hint": "Kombinasi 2 dari 6 objek"
            },
            {
                "id": "comb_3",
                "question": "Dari 10 soal, siswa harus mengerjakan 5 soal. Berapa banyak pilihan soal?",
                "answer": "252",
                "explanation": "C(10,5) = 10!/(5!×5!) = 252 pilihan",
                "hint": "Urutan pengerjaan soal tidak penting"
            }
        ]
    
    # ✅✅✅ METHOD RENDER_MODULE YANG PASTI ADA ✅✅✅
    def render_module(self, module_key):
        """Render a learning module"""
        # Dapatkan module data berdasarkan module_key
        module = self.modules.get(module_key)
        
        if not module:
            st.error(f"Module {module_key} tidak ditemukan!")
            return
        
        st.markdown(f"""
        <div class='learning-card' style='background: linear-gradient(135deg, {module['color']} 0%, {module['color']}77 100%);'>
            <h1>{module['title']}</h1>
            <h3>{module['description']}</h3>
            <p>Level: {module['level']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Explanation
        ai = DeepSeekAI()
        explanation = ai.get_ai_explanation(module_key, "beginner")
        st.markdown(f"""
        <div class='explanation-box'>
            {explanation}
        </div>
        """, unsafe_allow_html=True)
        
        # AI Tutor Chat
        st.markdown("### 🤖 AI Tutor - Tanya Apa Saja!")
        user_question = st.text_input("Punya pertanyaan tentang materi ini?", 
                                    placeholder="Tanyakan apa yang belum kamu pahami...",
                                    key=f"ai_tutor_{module_key}")
        
        if user_question:
            with st.spinner("AI Tutor sedang memikirkan jawaban..."):
                ai_response = ai.ask_ai_tutor(user_question, f"Konsep: {module['title']}")
                st.markdown(f"""
                <div class='explanation-box'>
                    <h4>🤖 Jawaban AI Tutor:</h4>
                    {ai_response}
                </div>
                """, unsafe_allow_html=True)
        
        # Practice Problems
        # Practice Problems - SUPER SIMPLE VERSION
        st.markdown("### 🎯 Latihan Praktik")
    
        problems = module.get('problems', [])
    
        for i, problem in enumerate(problems, 1):
            st.markdown(f"#### Soal {i}")
            st.markdown(f"**{problem['question']}**")
        
        # Input jawaban
            user_answer = st.text_input(
            "Jawaban Anda:",
                placeholder="Masukkan jawaban numerik...",
                key=f"input_{module_key}_{problem['id']}"
        )
        
        # Tombol cek - PAKAI FORM
        if st.button("✅ Cek Jawaban", key=f"check_{module_key}_{problem['id']}", type="primary"):
            if user_answer.strip() == "":
                st.warning("⚠️ Masukkan jawaban terlebih dahulu!")
            elif user_answer.strip() == problem['answer']:
                st.success(f"🎉 **BENAR!**")
                st.info(f"**Penjelasan:** {problem['explanation']}")
                research_system.update_learning_progress(module_key, True)
            else:
                st.error("❌ **Belum tepat**")
                st.info(f"💡 **Hint:** {problem['hint']}")
                research_system.update_learning_progress(module_key, False)
        
        st.markdown("---")
        
        # Module completion button
        st.markdown("---")
        complete_key = f"complete_{module_key}"
        if st.button("✅ Selesaikan Modul", key=complete_key, use_container_width=True, type="primary"):
            if research_system.complete_module(module_key):
                st.success(f"🎊 **Modul {module['title']} berhasil diselesaikan!**")
                show_celebration()
                st.session_state.current_module = None
                st.rerun()
            else:
                st.error("❌ Gagal menyelesaikan modul. Coba lagi.")
# ==================== VISUALIZATION FUNCTIONS ====================
def generate_sample_data():
    """Generate research data from REAL participant data"""
    try:
        participants_data = st.session_state.research_data['participants']
        
        if not participants_data:
            return _generate_fallback_data()
        
        participants = []
        for participant_id, data in participants_data.items():
            try:
                def safe_get(value, default=0):
                    if value is None:
                        return default
                    try:
                        return float(value) if value != '' else default
                    except (TypeError, ValueError):
                        return default
                
                pre_anxiety = safe_get(data.get('anxiety_survey', {}).get('pre_score'))
                post_anxiety = safe_get(data.get('anxiety_survey', {}).get('post_score'))
                pre_test_score = safe_get(data.get('pre_test', {}).get('score'))
                post_test_score = safe_get(data.get('post_test', {}).get('score'))
                
                anxiety_reduction = pre_anxiety - post_anxiety
                test_improvement = post_test_score - pre_test_score
                
                progress = data.get('learning_progress', {})
                attempted = safe_get(progress.get('problems_attempted'))
                correct = safe_get(progress.get('problems_correct'))
                
                if attempted > 0:
                    accuracy = (correct / attempted) * 100
                else:
                    accuracy = 0
                
                engagement = min(100, accuracy + 20)
                
                # Calculate time spent
                start_time = data.get('registration_time')
                if start_time:
                    start_dt = datetime.fromisoformat(start_time)
                    end_dt = datetime.now()
                    time_spent = (end_dt - start_dt).total_seconds() / 60
                else:
                    time_spent = 0
                
                participant = {
                    'id': participant_id,
                    'nama': data.get('demographics', {}).get('nama', 'Unknown'),
                    'kelas': data.get('demographics', {}).get('kelas', 'Unknown'),
                    'usia': data.get('demographics', {}).get('usia', 'Unknown'),
                    'pengalaman': data.get('demographics', {}).get('pengalaman', 'Unknown'),
                    'pre_anxiety': pre_anxiety,
                    'post_anxiety': post_anxiety,
                    'anxiety_reduction': anxiety_reduction,
                    'pre_test_score': pre_test_score,
                    'post_test_score': post_test_score,
                    'test_improvement': test_improvement,
                    'problems_attempted': attempted,
                    'problems_correct': correct,
                    'accuracy': accuracy,
                    'engagement': engagement,
                    'time_spent': time_spent,
                    'concepts_learned': len(progress.get('concepts_learned', [])),
                    'testimonial': data.get('satisfaction_survey', {}).get('testimonial', '')
                }
                participants.append(participant)
                
            except Exception as participant_error:
                continue
        
        if not participants:
            return _generate_fallback_data()
        
        return pd.DataFrame(participants)
        
    except Exception as e:
        return _generate_fallback_data()

def _generate_fallback_data():
    """Generate fallback data jika tidak ada data real"""
    try:
        np.random.seed(42)
        participants = []
        for i in range(3):
            participant = {
                'id': f'DEMO{i+1:03d}',
                'nama': f'Peserta Demo {i+1}',
                'pre_anxiety': max(20, min(85, np.random.normal(65, 12))),
                'post_anxiety': max(20, min(85, np.random.normal(50, 10))),
                'pre_test_score': max(0, min(5, np.random.normal(2.5, 1.5))),
                'post_test_score': max(0, min(5, np.random.normal(4.0, 0.8))),
                'problems_attempted': np.random.randint(15, 25),
                'problems_correct': np.random.randint(10, 20),
                'accuracy': max(0, min(100, np.random.normal(70, 8))),
                'engagement': max(0, min(100, np.random.normal(75, 5))),
                'time_spent': np.random.uniform(45, 120)
            }
            participant['anxiety_reduction'] = participant['pre_anxiety'] - participant['post_anxiety']
            participant['test_improvement'] = participant['post_test_score'] - participant['pre_test_score']
            
            participants.append(participant)
        
        return pd.DataFrame(participants)
    
    except Exception as e:
        return pd.DataFrame()

def render_individual_analytics():
    """Render individual participant analytics"""
    participant_data = st.session_state.participant_data
    
    if not participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu")
        return
    
    participant_id = participant_data['participant_id']
    timestamp = int(time.time() * 1000)  # Add timestamp for unique keys
    
    st.markdown("""
    <div class='research-card'>
        <h1>📈 Analisis Perkembangan Individual</h1>
        <p>Lihat perkembangan belajar dan pengurangan kecemasan matematika Anda.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        pre_score = participant_data['pre_test'].get('score', 0) or 0
        post_score = participant_data['post_test'].get('score', 0) or 0
        improvement = post_score - pre_score
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{improvement}</div>
            <div class='stat-label'>Peningkatan Nilai</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pre_anxiety = participant_data['anxiety_survey'].get('pre_score', 0) or 0
        post_anxiety = participant_data['anxiety_survey'].get('post_score', 0) or 0
        anxiety_reduction = pre_anxiety - post_anxiety
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{anxiety_reduction:.1f}</div>
            <div class='stat-label'>Pengurangan Kecemasan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        attempted = participant_data['learning_progress'].get('problems_attempted', 0)
        correct = participant_data['learning_progress'].get('problems_correct', 0)
        accuracy = (correct / attempted * 100) if attempted > 0 else 0
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{accuracy:.1f}%</div>
            <div class='stat-label'>Akurasi Belajar</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        time_spent = participant_data.get('time_spent_minutes', 0)
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{time_spent:.0f}m</div>
            <div class='stat-label'>Waktu Belajar</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts - FIXED: Use unique keys with timestamp
    col1, col2 = st.columns(2)
    
    with col1:
        # Test Score Improvement
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode = "number+delta",
            value = post_score,
            delta = {'reference': pre_score, 'relative': False},
            title = {"text": "Perkembangan Nilai Tes<br><span style='font-size:0.8em;color:gray'>Pre-test vs Post-test</span>"},
            domain = {'x': [0, 1], 'y': [0, 1]}
        ))
        fig.update_layout(height=200, margin=dict(l=10, r=10, t=50, b=10))
        st.plotly_chart(fig, use_container_width=True, key=f"indiv_chart1_{participant_id}_{timestamp}")
    
    with col2:
        # Anxiety Reduction
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode = "number+delta",
            value = post_anxiety,
            delta = {'reference': pre_anxiety, 'relative': False, 'increasing': {'color': "red"}, 'decreasing': {'color': "green"}},
            title = {"text": "Tingkat Kecemasan<br><span style='font-size:0.8em;color:gray'>Pre-survey vs Post-survey</span>"},
            domain = {'x': [0, 1], 'y': [0, 1]}
        ))
        fig.update_layout(height=200, margin=dict(l=10, r=10, t=50, b=10))
        st.plotly_chart(fig, use_container_width=True, key=f"indiv_chart2_{participant_id}_{timestamp}")

def render_global_analytics():
    """Render global research analytics"""
    df = generate_sample_data()
    
    if df.empty:
        st.info("📊 Data penelitian akan muncul di sini setelah peserta menyelesaikan program.")
        return
    
    timestamp = int(time.time() * 1000)  # Add timestamp for unique keys
    
    st.markdown('<div class="section-header">🌍 ANALISIS DATA GLOBAL</div>', unsafe_allow_html=True)
    
    # Global Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_improvement = df['test_improvement'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_improvement:.1f}</div>
            <div class="stat-label">Rata² Peningkatan Nilai</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        avg_anxiety_reduction = df['anxiety_reduction'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_anxiety_reduction:.1f}</div>
            <div class="stat-label">Rata² Pengurangan Kecemasan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_accuracy = df['accuracy'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_accuracy:.1f}%</div>
            <div class="stat-label">Rata² Akurasi</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_time = df['time_spent'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_time:.0f}m</div>
            <div class="stat-label">Rata² Waktu Belajar</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts - FIXED: Use unique keys with timestamp
    col1, col2 = st.columns(2)
    
    with col1:
        # Improvement Distribution
        fig = px.box(df, y='test_improvement', 
                    title='Distribusi Peningkatan Nilai Tes',
                    labels={'test_improvement': 'Peningkatan Nilai'})
        fig.update_traces(marker_color=COLORS['primary'])
        st.plotly_chart(fig, use_container_width=True, key=f"global_chart1_{timestamp}")
    
    with col2:
        # Anxiety Reduction Distribution
        fig = px.box(df, y='anxiety_reduction',
                    title='Distribusi Pengurangan Kecemasan',
                    labels={'anxiety_reduction': 'Pengurangan Kecemasan'})
        fig.update_traces(marker_color=COLORS['secondary'])
        st.plotly_chart(fig, use_container_width=True, key=f"global_chart2_{timestamp}")
    
    # Time vs Improvement Scatter
    fig = px.scatter(df, x='time_spent', y='test_improvement',
                    color='anxiety_reduction', size='accuracy',
                    hover_data=['nama'],
                    title='Hubungan Waktu Belajar vs Peningkatan Nilai',
                    labels={'time_spent': 'Waktu Belajar (menit)',
                           'test_improvement': 'Peningkatan Nilai',
                           'anxiety_reduction': 'Pengurangan Kecemasan'})
    st.plotly_chart(fig, use_container_width=True, key=f"global_chart3_{timestamp}")

# ==================== MAIN APPLICATION FUNCTIONS ====================
def render_dashboard():
    """Render main dashboard"""
    st.markdown("""
    <div class='research-card'>
        <h1>🌟 Selamat Datang di EasyNatorics!</h1>
        <p>Platform pembelajaran kombinatorika yang menggabungkan <strong>metakognisi, AI personalisasi, dan pendekatan berbasis penelitian</strong> untuk mengurangi kecemasan matematika.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>🔬 Metode</h3>
            <p>Penelitian Eksperimen dengan Pretest-Posttest Control Group Design</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>🎯 Fokus</h3>
            <p>Reduksi Kecemasan Matematika melalui Pembelajaran Metakognitif</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>🤖 Teknologi</h3>
            <p>AI Tutor & Adaptive Learning Path</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Continue button
    if st.button("🚀 Mulai Perjalanan Belajar", use_container_width=True, type="primary"):
        st.session_state.current_page = "Pendaftaran"
        st.rerun()

def render_registration():
    """Render participant registration form"""
    st.markdown("""
    <div class='research-card'>
        <h1>📝 Pendaftaran Peserta Penelitian</h1>
        <p>Isi data diri Anda untuk bergabung dalam penelitian ini. Data akan dijaga kerahasiaannya.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nama = st.text_input("Nama Lengkap*", placeholder="Masukkan nama lengkap")
            kelas = st.selectbox("Kelas*", ["10", "11", "12"])
        
        with col2:
            usia = st.number_input("Usia*", min_value=15, max_value=18, value=16)
            pengalaman = st.selectbox(
                "Pengalaman Belajar Matematika*",
                ["Pemula", "Menengah", "Lanjutan"]
            )
        
        consent = st.checkbox("Saya setuju untuk berpartisipasi dalam penelitian ini dan memahami bahwa data saya akan digunakan untuk tujuan akademik*")
        
        if st.form_submit_button("🚀 Daftar Sekarang", type="primary"):
            if not all([nama, kelas, usia, pengalaman, consent]):
                st.error("❌ Harap lengkapi semua field yang wajib diisi!")
            else:
                demographics = {
                    'nama': nama,
                    'kelas': kelas,
                    'usia': usia,
                    'pengalaman': pengalaman
                }
                
                participant_id = research_system.register_participant(demographics)
                if participant_id:
                    st.success(f"🎉 Pendaftaran berhasil! ID Anda: **{participant_id}**")
                    st.balloons()
                    st.session_state.current_page = "Survey Awal"
                    st.rerun()

def render_pre_survey(instruments):
    """Render pre-anxiety survey"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu di halaman Pendaftaran")
        return
    
    st.markdown("""
    <div class='research-card'>
        <h1>📊 Survey Kecemasan Matematika (Awal)</h1>
        <p>Survey ini mengukur tingkat kecemasan Anda terhadap matematika sebelum memulai pembelajaran.</p>
    </div>
    """, unsafe_allow_html=True)
    
    responses = instruments.render_amas_survey("pre")
    
    if st.button("📨 Submit Survey Awal & Lanjut ke Pre-Test", type="primary", use_container_width=True):
        amas_score = research_system.calculate_amas_score(responses)
        anxiety_level = research_system.get_anxiety_level(amas_score)
        
        st.session_state.participant_data['anxiety_survey']['pre_score'] = amas_score
        st.session_state.participant_data['anxiety_survey']['responses'] = responses
        
        st.success(f"""
        ✅ Survey berhasil disimpan!
        
        **Skor Kecemasan Awal:** {amas_score:.2f}
        **Tingkat Kecemasan:** {anxiety_level}
        """)
        
        st.session_state.current_page = "Pre-Test"
        st.rerun()

def render_pre_test(instruments):
    """Render pre-test assessment"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu di halaman Pendaftaran")
        return
    
    st.markdown("""
    <div class='test-card'>
        <h1>🎯 Pre-Test - Diagnosis Kemampuan Awal</h1>
        <p>Test ini mengukur pemahaman awal Anda tentang kombinatorika sebelum pembelajaran.</p>
    </div>
    """, unsafe_allow_html=True)
    
    answers, score = instruments.render_test("pre")
    
    if st.button("📊 Lihat Hasil Pre-Test & Lanjut Belajar", type="primary", use_container_width=True):
        st.session_state.participant_data['pre_test']['answers'] = answers
        st.session_state.participant_data['pre_test']['score'] = score
        st.session_state.participant_data['pre_test']['completion_time'] = datetime.now().isoformat()
        
        st.markdown(f"""
        <div class='success-card'>
            <h2>📊 Hasil Pre-Test</h2>
            <h1>{score}/5</h1>
            <h3>{score * 20}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state.current_page = "Belajar"
        st.rerun()

def render_learning_center(learning_modules):
    """Render interactive learning center"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu di halaman Pendaftaran")
        return
    
    st.markdown("""
    <div class='research-card'>
        <h1>📚 Pusat Pembelajaran Interaktif</h1>
        <p>Jelajahi dunia kombinatorika melalui modul-modul interaktif yang disesuaikan dengan kebutuhan Anda.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Pilih Modul Pembelajaran")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔢 Prinsip Perkalian", use_container_width=True, type="primary"):
            st.session_state.current_module = 'prinsip_perkalian'
    
    with col2:
        if st.button("🔄 Permutasi", use_container_width=True, type="primary"):
            st.session_state.current_module = 'permutasi'
    
    with col3:
        if st.button("👥 Kombinasi", use_container_width=True, type="primary"):
            st.session_state.current_module = 'kombinasi'
    
    if st.session_state.current_module:
        learning_modules.render_module(st.session_state.current_module)
    else:
        st.markdown("""
        <div class='learning-card'>
            <h2>🚀 Siap Memulai Perjalanan Belajar?</h2>
            <p>Pilih salah satu modul di atas untuk mulai menjelajahi konsep kombinatorika!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Continue to Post-Test button (only show if all modules completed)
    completed_modules = sum(1 for module in st.session_state.participant_data['learning_progress']['module_progress'].values() if module['completed'])
    if completed_modules >= 2:  # At least 2 modules completed
        if st.button("🎯 Lanjut ke Post-Test", type="primary", use_container_width=True):
            st.session_state.current_page = "Post-Test"
            st.rerun()

def render_post_test(instruments):
    """Render post-test assessment"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu di halaman Pendaftaran")
        return
    
    st.markdown("""
    <div class='test-card'>
        <h1>🚀 Post-Test - Evaluasi Peningkatan</h1>
        <p>Test ini mengukur peningkatan pemahaman Anda tentang kombinatorika setelah pembelajaran.</p>
    </div>
    """, unsafe_allow_html=True)
    
    answers, score = instruments.render_test("post")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Lihat Hasil Post-Test", type="primary", use_container_width=True):
            st.session_state.participant_data['post_test']['answers'] = answers
            st.session_state.participant_data['post_test']['score'] = score
            st.session_state.participant_data['post_test']['completion_time'] = datetime.now().isoformat()
            
            pre_score = st.session_state.participant_data['pre_test'].get('score', 0) or 0
            improvement = score - pre_score
            
            st.markdown(f"""
            <div class='success-card'>
                <h2>📊 Hasil Post-Test</h2>
                <h1>{score}/5</h1>
                <h3>{score * 20}%</h3>
                <h4>📈 Peningkatan: +{improvement} poin</h4>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if st.button("📝 Isi Survey Akhir", type="primary", use_container_width=True):
            st.session_state.current_page = "Survey Akhir"
            st.rerun()

def render_final_survey(instruments):
    """Render final anxiety survey and testimonial"""
    st.markdown("""
    <div class='research-card'>
        <h1>📊 Survey Kecemasan Akhir & Testimoni</h1>
        <p>Isi survey akhir dan berikan testimoni tentang pengalaman belajar Anda.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Survey Kecemasan Akhir")
    post_responses = instruments.render_amas_survey("post")
    
    st.markdown("### 💬 Testimoni")
    testimonial = st.text_area("Bagikan pengalaman belajar Anda dengan EasyNatorics:", 
                              placeholder="Apa yang paling Anda sukai? Apakah ada saran perbaikan?")
    
    if st.button("📨 Submit Semua & Lihat Hasil Akhir", type="primary", use_container_width=True):
        # Save post anxiety survey
        post_amas_score = research_system.calculate_amas_score(post_responses)
        st.session_state.participant_data['anxiety_survey']['post_score'] = post_amas_score
        
        # Save testimonial
        st.session_state.participant_data['satisfaction_survey']['testimonial'] = testimonial
        
        # Calculate final time spent
        start_time = st.session_state.participant_data.get('registration_time')
        if start_time:
            start_dt = datetime.fromisoformat(start_time)
            end_dt = datetime.now()
            time_spent = (end_dt - start_dt).total_seconds() / 60
            st.session_state.participant_data['time_spent_minutes'] = time_spent
        
        st.success("✅ Semua data berhasil disimpan! Terima kasih telah berpartisipasi.")
        st.session_state.current_page = "Hasil & Analisis"
        st.rerun()

def render_final_results():
    """Render final results with comprehensive analytics"""
    participant_data = st.session_state.participant_data
    
    st.markdown("""
    <div class='research-card'>
        <h1>📈 Hasil Akhir & Analisis Komprehensif</h1>
        <p>Lihat pencapaian dan perkembangan belajar Anda selama program penelitian.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Individual Analytics - FIXED: Only call this once
    render_individual_analytics()
    
    # Testimonial Display
    if participant_data['satisfaction_survey'].get('testimonial'):
        st.markdown("### 💬 Testimoni Anda")
        st.markdown(f"""
        <div class='testimonial-card'>
            <p>"{participant_data['satisfaction_survey']['testimonial']}"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Global Analytics
    render_global_analytics()
    
    # Data Export - FIXED VERSION
    st.markdown("---")
    st.markdown("### 📥 Export Data Penelitian")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Export Data Saya", type="primary", use_container_width=True):
            filename = DataExporter.export_participant_data(participant_data)
            if filename:
                st.success(f"✅ Data pribadi berhasil diexport ke: `{filename}`")
                show_celebration()
            else:
                st.error("❌ Gagal mengexport data pribadi")
    
    with col2:
        if st.button("📊 Export Semua Data", type="secondary", use_container_width=True):
            filename = DataExporter.export_all_research_data()
            if filename:
                st.success(f"✅ Semua data penelitian berhasil diexport!")
                show_celebration()
            else:
                st.error("❌ Gagal mengexport semua data")

def render_research_dashboard():
    """Render comprehensive research dashboard"""
    st.markdown("""
    <div class="main-title">EASYNATORICS RESEARCH FINDINGS</div>
    <div style="text-align: center; color: #00D4FF; font-size: 1.2rem; margin-bottom: 1rem;">
        ANALISIS DATA PENELITIAN KOMPREHENSIF
    </div>
    """, unsafe_allow_html=True)
    
    # Global Analytics
    render_global_analytics()
    
    # Individual Analytics for current participant
    if st.session_state.participant_data['participant_id']:
        st.markdown('<div class="section-header">👤 ANALISIS INDIVIDUAL</div>', unsafe_allow_html=True)
        render_individual_analytics()

# ==================== MAIN APPLICATION ====================
def main():
    # Initialize systems
    global research_system, data_exporter
    research_system = ResearchDataSystem()
    instruments = ResearchInstruments()
    learning_modules = LearningModules()
    data_exporter = DataExporter()
    
    apply_futuristic_style()
    
    # Initialize session state for navigation
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Dashboard"
    
    # Main title with animations
    st.markdown("""
    <div class="main-title">
        EasyNatorics
    </div>
    <div style="text-align: center; color: #00D4FF; font-size: 1.5rem; margin-bottom: 3rem;">
        Jelajah Kombinatorika dengan Metakognisi & AI
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h2 style="color: #00D4FF;">🧭 Navigasi</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.participant_data['participant_id']:
            participant_id = st.session_state.participant_data['participant_id']
            st.success(f"👤 Participant: {participant_id}")
        
        # Navigation options with proper mapping
        nav_options = [
            "🏠 Dashboard", 
            "📝 Pendaftaran", 
            "📊 Survey Awal",
            "🎯 Pre-Test", 
            "📚 Belajar", 
            "🚀 Post-Test",
            "📝 Survey Akhir",
            "📈 Hasil & Analisis",
            "🔬 Research Dashboard"
        ]
        
        # Create mapping between display names and internal page names
        page_mapping = {
            "🏠 Dashboard": "Dashboard",
            "📝 Pendaftaran": "Pendaftaran", 
            "📊 Survey Awal": "Survey Awal",
            "🎯 Pre-Test": "Pre-Test",
            "📚 Belajar": "Belajar",
            "🚀 Post-Test": "Post-Test", 
            "📝 Survey Akhir": "Survey Akhir",
            "📈 Hasil & Analisis": "Hasil & Analisis",
            "🔬 Research Dashboard": "Research Dashboard"
        }
        
        # Get current display name
        current_display = [k for k, v in page_mapping.items() if v == st.session_state.current_page]
        default_index = 0
        if current_display:
            default_index = nav_options.index(current_display[0])
        
        selected_nav = st.radio("Pilih Tahapan:", nav_options, index=default_index)
        
        # Update current page based on selection
        st.session_state.current_page = page_mapping[selected_nav]
    
    # Page routing based on current_page
    if st.session_state.current_page == "Dashboard":
        render_dashboard()
    elif st.session_state.current_page == "Pendaftaran":
        render_registration()
    elif st.session_state.current_page == "Survey Awal":
        render_pre_survey(instruments)
    elif st.session_state.current_page == "Pre-Test":
        render_pre_test(instruments)
    elif st.session_state.current_page == "Belajar":
        render_learning_center(learning_modules)
    elif st.session_state.current_page == "Post-Test":
        render_post_test(instruments)
    elif st.session_state.current_page == "Survey Akhir":
        render_final_survey(instruments)
    elif st.session_state.current_page == "Hasil & Analisis":
        render_final_results()
    elif st.session_state.current_page == "Research Dashboard":
        render_research_dashboard()

# ==================== RUN APPLICATION ====================
if __name__ == "__main__":
    main()