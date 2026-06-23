# -*- coding: utf-8 -*-
"""Bharat Direct — square LinkedIn carousel (PDF, 1080x1080)."""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Fonts (Arial has the rupee glyph; fall back to Helvetica)
BOLD, REG = 'Helvetica-Bold', 'Helvetica'
try:
    pdfmetrics.registerFont(TTFont('AR', r'C:\Windows\Fonts\arial.ttf'))
    pdfmetrics.registerFont(TTFont('ARB', r'C:\Windows\Fonts\arialbd.ttf'))
    BOLD, REG = 'ARB', 'AR'
except Exception as e:
    print('font fallback:', e)

NAVY = HexColor('#11183A')
NAVY2 = HexColor('#1B2555')
AMBER = HexColor('#F4A81D')
ICE = HexColor('#CADCFC')
WHITE = HexColor('#FFFFFF')
GREY = HexColor('#9AA3B8')

S = 1080
M = 90  # margin
out = r'C:\Users\dhire\OneDrive\Documents\00 Dhirendra\Innovations\Payment Innovation\Bharat Direct\Bharat-Direct-Carousel.pdf'
c = canvas.Canvas(out, pagesize=(S, S))

def wrap(text, font, size, maxw):
    words = text.split(' '); lines=[]; cur=''
    for w in words:
        t = (cur+' '+w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def draw_para(text, x, y, font, size, color, maxw, leading=None, align='left'):
    leading = leading or size*1.12
    c.setFont(font, size); c.setFillColor(color)
    for ln in wrap(text, font, size, maxw):
        if align=='center':
            c.drawCentredString(S/2, y, ln)
        else:
            c.drawString(x, y, ln)
        y -= leading
    return y

def bg(color=NAVY):
    c.setFillColor(color); c.rect(0,0,S,S,fill=1,stroke=0)

def footer(page, total=11, dark_bg=True):
    c.setFont(BOLD, 22); c.setFillColor(AMBER)
    c.drawString(M, M-30, 'BHARAT DIRECT')
    c.setFont(REG, 22); c.setFillColor(GREY if dark_bg else HexColor('#6B7280'))
    c.drawRightString(S-M, M-30, f'{page} / {total}')

def chip(text, x, y, color=AMBER, txt=NAVY):
    w = pdfmetrics.stringWidth(text, BOLD, 22)+44
    c.setFillColor(color); c.roundRect(x, y, w, 50, 14, fill=1, stroke=0)
    c.setFont(BOLD, 22); c.setFillColor(txt)
    c.drawString(x+22, y+16, text)
    return w

def page_end(n): footer(n); c.showPage()

# ---------- 1 HOOK ----------
bg(NAVY)
c.setFillColor(AMBER); c.rect(M, 980, 120, 12, fill=1, stroke=0)
draw_para('India built', M, 760, REG, 64, ICE, S-2*M)
draw_para('UPI.', M, 690, BOLD, 96, WHITE, S-2*M)
y = draw_para('Two things still', M, 560, BOLD, 70, WHITE, S-2*M, leading=82)
draw_para('cost you.', M, y+8, BOLD, 70, AMBER, S-2*M)
draw_para('A rent you don’t see — and a fraud no faster rail can stop.', M, 300, REG, 30, GREY, S-2*M, leading=40)
footer(1); c.showPage()

# ---------- 2 TOLL-BOOTH ----------
bg(NAVY)
chip('THE TOLL-BOOTH', M, 900)
draw_para('A middleman still', M, 760, BOLD, 60, WHITE, S-2*M, leading=72)
y=draw_para('takes a cut of', M, 700, BOLD, 60, WHITE, S-2*M, leading=72)
draw_para('every payment —', M, y+10, BOLD, 60, WHITE, S-2*M, leading=72)
draw_para('even though the money can move bank-to-bank, with no aggregator in the path.', M, 470, REG, 34, ICE, S-2*M, leading=46)
draw_para('UPI already proves it. We just haven’t finished the job.', M, 290, REG, 30, GREY, S-2*M, leading=40)
footer(2); c.showPage()

# ---------- 3 FRAUD GAP ----------
bg(NAVY)
chip('THE FRAUD GAP', M, 900, color=AMBER)
draw_para('The scam isn’t', M, 770, BOLD, 62, WHITE, S-2*M)
draw_para('hacking your', M, 700, BOLD, 62, WHITE, S-2*M)
draw_para('account.', M, 630, BOLD, 62, AMBER, S-2*M)
draw_para('It’s talking YOU into paying. A faster rail does nothing to stop that.', M, 470, REG, 34, ICE, S-2*M, leading=46)
draw_para('This is now the fastest-growing financial crime in the country.', M, 290, REG, 30, GREY, S-2*M, leading=40)
footer(3); c.showPage()

# ---------- 4 PSYCHOLOGY ----------
bg(WHITE)
chip('WHY YOU FALL FOR IT', M, 900, color=NAVY, txt=WHITE)
draw_para('You knew better.', M, 770, BOLD, 58, NAVY, S-2*M)
draw_para('Your brain just', M, 705, BOLD, 58, NAVY, S-2*M)
draw_para('didn’t get the memo.', M, 640, BOLD, 58, AMBER, S-2*M)
draw_para('A scam triggers panic. Panic shuts down judgment. In that state you literally can’t reach what you already know.', M, 470, REG, 34, HexColor('#1A1F2E'), S-2*M, leading=46)
draw_para('"Don’t hang up. Don’t tell anyone. Do it now." — one voice, no second opinion.', M, 270, REG, 30, HexColor('#5A6070'), S-2*M, leading=40)
footer(4, dark_bg=False); c.showPage()

# ---------- 5 CHOKEPOINT ----------
bg(NAVY)
chip('THE ONE MOMENT', M, 900)
draw_para('Every scam ends', M, 740, BOLD, 60, WHITE, S-2*M)
draw_para('at the same click:', M, 670, BOLD, 60, WHITE, S-2*M)
draw_para('you authorising', M, 560, BOLD, 64, AMBER, S-2*M, leading=74)
draw_para('the payment.', M, 490, BOLD, 64, AMBER, S-2*M)
draw_para('You can’t stop the call. You CAN intervene at that one click — for two seconds.', M, 320, REG, 33, ICE, S-2*M, leading=44)
footer(5); c.showPage()

# ---------- 6 WHY ADS FAIL ----------
bg(NAVY)
chip('WHY ADS FAIL', M, 900)
draw_para('A "beware of fraud"', M, 770, BOLD, 54, WHITE, S-2*M)
draw_para('banner on every', M, 710, BOLD, 54, WHITE, S-2*M)
draw_para('screen becomes', M, 650, BOLD, 54, WHITE, S-2*M)
draw_para('wallpaper.', M, 590, BOLD, 54, AMBER, S-2*M)
c.setFillColor(NAVY2); c.roundRect(M, 360, S-2*M, 170, 18, fill=1, stroke=0)
draw_para('Warnings must be rare, specific, and earned by real risk — or they’re worse than nothing.', M+40, 470, BOLD, 32, WHITE, S-2*M-80, leading=42)
draw_para('Which means you need shared intelligence to know when to fire.', M, 280, REG, 29, GREY, S-2*M, leading=40)
footer(6); c.showPage()

# ---------- 7 AWARE LAYER ----------
bg(WHITE)
chip('THE FIX, PART 1', M, 900, color=NAVY, txt=WHITE)
draw_para('The Aware Layer', M, 800, BOLD, 60, NAVY, S-2*M)
draw_para('The screen becomes the second voice in the room.', M, 740, REG, 30, HexColor('#5A6070'), S-2*M)
items = [
 'A cooling countdown that breaks the scammer’s urgency',
 '"Is someone on the phone telling you to pay right now?"',
 '"This matches a digital-arrest scam" — named, not vague',
 '"This account: 9 fraud reports in 24h" at the confirm screen',
]
y = 640
for i,it in enumerate(items):
    c.setFillColor(AMBER); c.circle(M+22, y-2, 22, fill=1, stroke=0)
    c.setFont(BOLD, 26); c.setFillColor(NAVY); c.drawCentredString(M+22, y-11, str(i+1))
    draw_para(it, M+70, y+5, REG, 30, HexColor('#1A1F2E'), S-2*M-70, leading=40)
    y -= 120
footer(7, dark_bg=False); c.showPage()

# ---------- 8 FIC ----------
bg(NAVY)
chip('THE FIX, PART 2', M, 900)
draw_para('A Fraud', M, 800, BOLD, 64, WHITE, S-2*M)
draw_para('Intelligence', M, 730, BOLD, 64, WHITE, S-2*M)
draw_para('Consortium', M, 660, BOLD, 64, AMBER, S-2*M)
draw_para('Fraud is a network crime fought by isolated banks. Each sees one sliver; the criminal sees the whole map.', M, 520, REG, 32, ICE, S-2*M, leading=44)
draw_para('Pool the signal (not the data). Flag a mule at one bank — every bank knows in seconds.', M, 360, REG, 32, WHITE, S-2*M, leading=44)
draw_para('Make the bank that hosts a mule share the loss. Then sharing becomes self-interest.', M, 220, REG, 28, GREY, S-2*M, leading=38)
footer(8); c.showPage()

# ---------- 9 WHO GAINS ----------
bg(WHITE)
chip('WHO GAINS', M, 900, color=NAVY, txt=WHITE)
draw_para('Almost everyone.', M, 800, BOLD, 60, NAVY, S-2*M)
rows = [
 ('Merchants','flat near-zero cost, not a percentage'),
 ('Banks','own the rail + the revenue middlemen take today'),
 ('Government','lower subsidy, sovereignty, protected citizens'),
 ('You','lower prices and far less chance of being scammed'),
]
y = 680
for h,b in rows:
    c.setFillColor(HexColor('#EEF1F7')); c.roundRect(M, y-70, S-2*M, 110, 16, fill=1, stroke=0)
    c.setFont(BOLD, 34); c.setFillColor(NAVY); c.drawString(M+34, y-8, h)
    c.setFont(REG, 26); c.setFillColor(HexColor('#1A1F2E')); c.drawString(M+34, y-48, b)
    y -= 140
footer(9, dark_bg=False); c.showPage()

# ---------- 10 THE ASK ----------
bg(NAVY)
chip('THE ASK', M, 900)
draw_para('India built the', M, 760, BOLD, 58, WHITE, S-2*M)
draw_para('hardest 80%.', M, 695, BOLD, 58, WHITE, S-2*M)
draw_para('Let’s finish it —', M, 560, BOLD, 62, AMBER, S-2*M, leading=74)
draw_para('together.', M, 490, BOLD, 62, AMBER, S-2*M)
draw_para('A pre-competitive working group: RBI, NPCI, CERSAI, banks, cybercrime (1930), fintechs and researchers.', M, 330, REG, 32, ICE, S-2*M, leading=44)
draw_para('Pilot the fraud win first. Then remove the toll-booth.', M, 200, REG, 28, GREY, S-2*M, leading=38)
footer(10); c.showPage()

# ---------- 11 CTA ----------
bg(AMBER)
draw_para('If this makes', M, 720, BOLD, 76, NAVY, S-2*M, leading=86)
draw_para('sense to you —', M, 640, BOLD, 76, NAVY, S-2*M)
draw_para('Comment. Repost. Tag the one person who should be in the room.', M, 470, REG, 38, NAVY, S-2*M, leading=50)
c.setFont(BOLD, 30); c.setFillColor(NAVY)
c.drawString(M, M, 'BHARAT DIRECT  ·  a discussion starter, not a pitch for sale')
c.showPage()

c.save()
print('Saved carousel:', out)
