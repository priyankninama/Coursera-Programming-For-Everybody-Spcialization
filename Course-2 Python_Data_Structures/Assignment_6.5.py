text = "X-DSPAM-Confidence: 0.8475"
i=text.find (':')
p=text[i+2:]
value=float(p)
print(value)