from django.db import models as m


# какие колонки с какой таблицы читать - (Model)
# булем испольовать постгиэс (postgies)
class UserInfo(m.Model):
    name = m.TextField(unique=True)
    greeting = m.TextField(null=True, blank=True)
    age = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User Info"  # выставл прав имя а не джанго дичку

        def __str__(self):
            return f"UserInfo(id={self.pk},name={self.name!r})"




#a = UserInfo()  - где 'а' это объект
#b = UserInfo()
#print(a.name)
#print(b.name)

