import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

output_pdf = "/Users/apple/.gemini/antigravity-ide/scratch/ibm_skillsbuild_final_submission/concept_note/Concept_Note_Document.pdf"

# Read markdown text
md_path = "/Users/apple/.gemini/antigravity-ide/scratch/ibm_skillsbuild_final_submission/concept_note/Concept_Note_Document.md"
with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with PdfPages(output_pdf) as pdf:
    # Page setup
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.axis('off')
    
    y = 0.95
    line_height = 0.021
    
    for line in lines:
        raw_line = line.strip()
        if not raw_line:
            y -= line_height * 0.8
            continue
        
        # Check page overflow
        if y < 0.08:
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()
            fig, ax = plt.subplots(figsize=(8.5, 11), dpi=300)
            fig.patch.set_facecolor('#ffffff')
            ax.axis('off')
            y = 0.95
            
        font_size = 9.5
        font_weight = 'normal'
        color = '#1e293b'
        indent = 0.08
        
        if raw_line.startswith('# '):
            font_size = 15
            font_weight = 'bold'
            color = '#001d6c'
            text = raw_line[2:]
            y -= 0.01
        elif raw_line.startswith('## '):
            font_size = 12
            font_weight = 'bold'
            color = '#0f62fe'
            text = raw_line[3:]
            y -= 0.008
        elif raw_line.startswith('### '):
            font_size = 10.5
            font_weight = 'bold'
            color = '#0f172a'
            text = raw_line[4:]
        elif raw_line.startswith('---'):
            ax.plot([0.08, 0.92], [y, y], color='#cbd5e1', lw=1)
            y -= line_height
            continue
        elif raw_line.startswith('* '):
            text = "• " + raw_line[2:]
            indent = 0.11
        elif raw_line.startswith('• '):
            text = raw_line
            indent = 0.11
        else:
            text = raw_line
            
        # Clean bold markers for cleaner plain text rendering
        text = text.replace('**', '').replace('`', '')
        
        # Word wrap if too long
        if len(text) > 88:
            words = text.split(' ')
            sub_lines = []
            curr = ""
            for w in words:
                if len(curr + " " + w) <= 88:
                    curr += (" " + w if curr else w)
                else:
                    sub_lines.append(curr)
                    curr = w
            if curr:
                sub_lines.append(curr)
                
            for sl in sub_lines:
                if y < 0.08:
                    pdf.savefig(fig, bbox_inches='tight')
                    plt.close()
                    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=300)
                    fig.patch.set_facecolor('#ffffff')
                    ax.axis('off')
                    y = 0.95
                ax.text(indent, y, sl, fontsize=font_size, fontweight=font_weight, color=color, va='top')
                y -= line_height
        else:
            ax.text(indent, y, text, fontsize=font_size, fontweight=font_weight, color=color, va='top')
            y -= line_height

    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

print("Concept Note PDF created successfully at:", output_pdf)
