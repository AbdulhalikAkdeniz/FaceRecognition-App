import os

def main():
    folder_path = 'uploaded_images/'  # Kendi klasör yolunuzu buraya yazın

# Klasördeki tüm dosyaları dolaş
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Eğer dosya ise, sil
        if os.path.isfile(file_path):
            os.remove(file_path)  # Dosyayı sil

    print("uploaded_images deleted")

    folder_path2 = 'uploaded_videos/'  # Kendi klasör yolunuzu buraya yazın

# Klasördeki tüm dosyaları dolaş
    for filename2 in os.listdir(folder_path2):
        file_path2 = os.path.join(folder_path2, filename2)
        
        # Eğer dosya ise, sil
        if os.path.isfile(file_path2):
            os.remove(file_path2)  # Dosyayı sil

    print("uploaded_videos deleted")