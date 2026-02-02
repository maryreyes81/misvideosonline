from django.db import models


class TBL_Usuario(models.Model):
    # Django crea un id numérico automático como PK (id)
    nomina = models.CharField(max_length=10, unique=True)  # llave lógica (alfanumérico 10)
    nombre = models.CharField(max_length=50)               # alfanumérico 50

    class Meta:
        db_table = "TBL_Usuario"

    def __str__(self) -> str:
        return f"{self.nomina} - {self.nombre}"


class TBL_Video(models.Model):
    # Django crea id automático para el video (id)
    nombre_video = models.CharField(max_length=50)  # alfanumérico 50
    extension = models.CharField(max_length=5)      # alfanumérico 5
    tamano = models.IntegerField()                  # numérico

    class Meta:
        db_table = "TBL_Video"

    def __str__(self) -> str:
        return f"{self.nombre_video}.{self.extension} ({self.tamano}MB)"


class TBL_UsuarioVideo(models.Model):
    # Tabla puente usuario-video
    usuario = models.ForeignKey(TBL_Usuario, on_delete=models.CASCADE)
    video = models.ForeignKey(TBL_Video, on_delete=models.CASCADE)

    class Meta:
        db_table = "TBL_UsuarioVideo"
        unique_together = ("usuario", "video")