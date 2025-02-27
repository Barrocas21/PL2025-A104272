import re

def markdown_to_html(md_text):
    # Cabeçalhos
    md_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    
    # Bold
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)
    
    # Itálico
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)
    
    # Links
    md_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', md_text)
    
    # Imagens
    md_text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', md_text)
    
    # Listas numeradas
    def replace_ordered_list(match):
        items = match.group().split('\n')
        list_items = ''.join(f'<li>{item[3:]}</li>' for item in items if item)
        return f'<ol>{list_items}</ol>'
    
    md_text = re.sub(r'(?:^\d+\. .+(?:\n|$))+', replace_ordered_list, md_text, flags=re.MULTILINE)
    
    return md_text

