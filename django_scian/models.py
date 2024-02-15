from django.db import models
from treenode.models import TreeNodeModel

class SCIAN(TreeNodeModel):
    """
    El Sistema de Clasificación Industrial de América del Norte (SCIAN) 
    es un sistema de clasificación de códigos numéricos que se utiliza 
    para identificar las actividades económicas en México, Canadá y Estados Unidos. 
    El SCIAN es una herramienta que permite a los países comparar estadísticas 
    de producción, empleo, inversión, entre otros, en un marco de referencia común.
    """

    treenode_display_field = "titulo"
    nivel = models.CharField(max_length=16, choices=(('sector', 'Sector'), ('subsector', 'Subsector'), ('rama', 'Rama'), ('subrama', 'Subrama'), ('clase', 'Clase')))
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True,)
    incluye = models.TextField(blank=True, null=True)
    excluye = models.TextField(blank=True, null=True)
    indice = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " - " + self.titulo

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Taxón"
        verbose_name_plural = "Taxonomía"
        ordering = ['id']
