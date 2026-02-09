import os
def extract_number(filename):
    return int(filename.split('.')[0])
try:
    for i in range(1, 162):
        frames_folder = f"t/top-tier/top-tier-providence-secretly-cultivate-for-a-thousand-years-chapter-{i}"
        title = f"top-tier{i}"
        frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.webm')])
        sorted_data = sorted(frame_files, key=extract_number)
        file_path = f"{frames_folder}/a.html" 
        if os.path.exists(file_path):
            os.unlink(file_path)
        else:
            print(f'not found {file_path}')
        with open(file_path, 'w') as file:
            file.write(f'<html><meta name="color-scheme" content="light dark"><meta name="viewport" content="width=device-width, initial-scale=1"><head><title>{title}</title></head><body>\n')
            file.write(f"<h2>{title}</h2>\n")
            for im in sorted_data:
                file.write(f'<img src="{im}" alt="{im}" width="100%">\n')
            file.write('<script>function myFunction() {   var element = document.body;   element.classList.toggle("dark-mode");}</script>')
            file.write('<style>img {  display: block;  margin-left: auto;  margin-right: auto;}</style>')
            file.write("</body></html>\n")
except Exception as e:
    print(f'error {e}')
