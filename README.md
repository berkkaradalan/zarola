# zarola

Zarola nedir?
Parola nedir?
Parola, en basit şekilde bir sisteme veya alana girmeye çalışan kişinin gerçekten o kişi olduğunu doğrulamayı sağlayan, bir grup kelime veya karakterden oluşan öbek olarak tanımlanabilir.

Parolalar nerelerde kullanılır?
Kablosuz ağlara giriş için WEP, WPA veya WPA2 gibi güvenlik sistemlerinde kullanılır. Bu sistemlerin güvenliği parolanızın gücüne bağlıdır.
Çevrimiçi kullanıcı hesaplarına giriş yaparken parolalar kullanılır. Örneğin e-posta hesabınıza girerken, sosyal ağlara bağlanırken veya kamu uygulamalarını kullanırken parola ile giriş yaparsınız.
GnuPG gibi şifreleme araçları, anahtarların güvenliği için parola kullanır. Gizli anahtarınızı kullanırken parola girmeniz istenir.
Bilgisayarınızın sabit diskini şifrelediğinizde, her açılışta parola girmeniz gerekir.
Bitcoin gibi kriptodövizler, cüzdanlarına erişim için parola sormaktadır.
“Güvenlik sorusu” olarak bilinen parola kurtarma soruları da yine parola sayılabilir. Bu tarz sorular için de gerçek cevaplar yerine parola koymak güvenliği artıracaktır.
Güvenli bir parola şu özellikleri taşımalıdır:

Sadece sahibi tarafından bilinmelidir.
Güvenli olacak kadar uzun olmalıdır.
Sahibini çok iyi tanıyan insanlar tarafından dahi tahmin edilmesi çok zor olmalıdır.
Sahibi için hatırlaması kolay olmalıdır.
Her türlü sistemde kolayca yazılabilmelidir.
Zarola, paroladan farklı ne sunuyor?
Genellikle, parolalar altı ila on karakter arasında alfanümerik olarak kullanılır. Bu tarz parolalar sürekli denetim altında olan sistemler için kullanılabilir, ancak anahtar güvenliği için yeterli değildir. Uzun ve güvenli (30 karakter, alfanümerik+özel karakterler) bir parolayı hem oluşturmak hem de hatırlamak çok zordur.

Zarola, güvenli ve hatırlanabilir parolalar oluşturmanızı sağlayan bir yöntemdir. Parolaları oluştururken zarlar ve kelime listesinden yararlanılır. Kelime listesinde yer alan her kelime, 11111 ile 66666 arasında beş haneli bir numaraya sahiptir.

Örnek kelime listesi:

14236	asamble
14241	asap
14242	asar
14243	asbest
14244	asepsi
14245	ases
14246	asetat
14251	asetik
14252	aseton
14253	asfalt
14254	ashap
14255	asi
14256	aside
14261	asil
14262	asistan
14263	asit
14264	ask
14265	askarit
14266	asker
14311	asla
14312	aslan
14313	aslen
14314	asliye
Listede toplam 7776 kısa kelime ve işaret bulunmaktadır. Türkçe için sunulan kelime listesi Alper Atmaca tarafından oluşturulmuştur.

Zarola şifreleri kendi sitesinden oluşturmak daha sağlıklıdır. Resmi Zarola sitesi aşağıdadır.

https://zarola.oyd.org.tr/

Benim hazırlamış olduğum kod içeriğinde fiziksel bir zara sahip olmadan zar atışı yapılır (rastgele sayı üretilir) ve oluşturulan değerlere karşılık gelen kelimeleri ekrana çıktı olarak verir. Programı çalıştırdığınızda sizden 5 rakamına tam bölünebilen bir sayı girmenizi istyecek bunun nedeni listdeki kelimelerin beşer hane ile bölünmüş olmasıdır örneğin;
//14314	asliye
asliye kelimesini elde etmek için elimizdeki fiziksel zar ile sırasıyla 1-4-3-1-4 atmamız gerekecekti.
