Pytest Decoratörler

PyTest, Python için popüler bir test çerçevesidir.
PyTest kullanarak, Python kodunuzun testlerini kolayca yazabilir ve çalıştırabiliriz.
Pytest testlerinizi yazarken, testlerinizi dekore ederek belirli özellikleri test etmenizi sağlayan bir dizi dekoratör sağlar:

1)@pytest.fixture: Bu dekoratör, test fonksiyonlarına ek veri sağlamak için kullanılır.
Fixture fonksiyonları, testlerinize belirli bir durum sağlamak için kullanışlıdır.
Örneğin, bir testte veritabanı bağlantısını kullanmak istiyorsanız, @pytest.fixture kullanarak bağlantıyı oluşturabilirsiniz.

2)@pytest.mark.parametrize: Bu dekoratör, test fonksiyonlarınızı belirli parametrelerle çalıştırmanızı sağlar.
Böylece, bir testi farklı veri setleriyle çalıştırarak, farklı durumlarda nasıl davrandığını test edebilirsiniz.
Örneğin, bir testinizi farklı girdilerle çalıştırarak, girdi değerlerinin sonucu nasıl etkilediğini test edebilirsiniz.

3)@pytest.mark.skip: Bu dekoratör, belirli bir testi atlamak için kullanılır.
Bu dekoratörü kullanarak, örneğin bir testin belirli bir sürümde hatalı olduğunu
belirleyebilirsiniz ve testi geçici olarak atlayabilirsiniz.

4)@pytest.mark.xfail: Bu dekoratör, belirli bir testin başarısız olmasını beklediğinizi belirtmek için kullanılır.
Bu dekoratörü kullanarak, örneğin bir hata düzeltildikten sonra testin tekrar çalıştırılması gerektiğinde testinizi işaretleyebilirsiniz.

5)@pytest.mark.timeout: Bu dekoratör, belirli bir testin ne kadar sürede tamamlanması gerektiğini belirlemek için kullanılır.
Bu dekoratörü kullanarak, testlerinizin ne kadar sürede tamamlandığını kontrol edebilir ve uzun süren testlerinizi belirleyebilirsiniz.

Yukarıda bahsedilen dekoratörler, PyTest'te kullanılan en yaygın dekoratörlerdir.
Ancak, PyTest'te kullanabileceğiniz birçok dekoratör vardır ve ihtiyaçlarınıza göre farklı dekoratörler kullanabilirsiniz.
İnternetten veya direkt olarak Pytest'in resmi sitesinden yapacağınız küçük bir araştırma ile daha fazlasını bulmak mümkün.
Kolay gelsin! :)
