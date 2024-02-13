from django.db import models

# Create your models here.

from treenode.models import TreeNodeModel

class SCIAN(TreeNodeModel):

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
