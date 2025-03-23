import ezdxf

class DXFLoader:
    def __init__(self, file_path):
        self.doc = ezdxf.readfile(file_path)
        self.msp = self.doc.modelspace()

    def get_entities(self, entity_type="LINE"):
        """Επιστρέφει όλες τις γραμμές (ή άλλα entities) από το DXF."""
        return [entity for entity in self.msp.query(entity_type)]

    def get_all_layers(self):
        """Επιστρέφει όλα τα layers από το DXF."""
        return [layer.dxf.name for layer in self.doc.layers]
