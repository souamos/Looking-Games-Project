import Jogo_Model
from Jogo_Model import Jogo
import Jogo_Dal


def jogo_select(jogo):
    jogoquery = Jogo_Model.Jogo
    jogoquery = Jogo_Dal.db_select(jogo)
    return jogoquery





