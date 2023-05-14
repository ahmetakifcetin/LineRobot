# Otonom Hat Takip Eden Robot

- Bu proje, Raspberry Pi, motor sürücü kartı ve sensörler kullanarak otonom bir hat takip eden robot yapmayı amaçlar. Robot, sol ve sağ sensörler aracılığıyla bir çizgiyi takip eder ve hareketini buna göre kontrol eder.

## Gereksinimler

- Raspberry Pi
- Motor sürücü kartı
- Sol ve sağ sensörler
- Python 3
- RPi.GPIO kütüphanesi

## Kurulum

1. Raspberry Pi'ye Raspbian işletim sistemini yükleyin.
2. Gerekli donanım bileşenlerini bağlayın: motor sürücü kartı, sol ve sağ sensörler.
3. Terminali açın ve aşağıdaki komutu çalıştırarak RPi.GPIO kütüphanesini yükleyin:
4. Proje dosyalarını Raspberry Pi'ye kopyalayın veya bu projenin bir klonunu alın.

## Bağlantılar

- Sol sensör: GPIO pin numarası X
- Sağ sensör: GPIO pin numarası Y
- Sol motor ileri: GPIO pin numarası A
- Sol motor geri: GPIO pin numarası B
- Sağ motor ileri: GPIO pin numarası C
- Sağ motor geri: GPIO pin numarası D

Gerekli GPIO pin numaralarını `main.py` dosyasında uygun şekilde güncelleyin.

## Kullanım

1. Terminalde proje dizinine gidin.
2. Aşağıdaki komutu çalıştırarak robotu çalıştırın:
3. Robot, sensör verilerini kullanarak çizgiyi takip edecek ve hareketini buna göre kontrol edecektir.
4. Robotu durdurmak için `Ctrl+C` tuş kombinasyonunu kullanabilirsiniz.

## Katkılar

- Katkılarınızı memnuniyetle karşılıyoruz! Herhangi bir hata düzeltmesi, iyileştirme veya yeni özellik eklemek için e-posta adresimden bana ulaşabilirsiniz.

## Lisans

- Bu proje MIT Lisansı altında lisanslanmıştır. 
• Daha fazla bilgi için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.
