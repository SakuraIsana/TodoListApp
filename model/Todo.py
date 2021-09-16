class Todo():

    def __init__(self,id_t,desc):
        self._id_t = id_t
        self._description = desc

    def _set_id(self,new_id):
        self._id = new_id

    def _get_id(self):
        return self._id

    def _set_description(self,desc):
        self._description = desc

    def _get_description(self):
        return self._description

    id_t = property(_get_id,_set_id)
    description = property(_get_description,_set_description)