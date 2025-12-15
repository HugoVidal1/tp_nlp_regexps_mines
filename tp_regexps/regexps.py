import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')

#
# Regexps pour le bloc titre
#
title_re = None  # TODO

#
# Regexps pour le "header"
#
# Le bloc "header" est de la forme:
#
#<div class="decision-header">
# <p class="h4-like">Troisième chambre civile
#                          -
#              Formation restreinte RNSM/NA
#                      </p>
#                              <p class="h4-like h4-like--emphase">
#                      </p>
#          <p>ECLI:FR:CCASS:2024:C310675</p>
#        </div>
#
header_re = re.compile(r'<div\s+class="decision-header">(?P<header>.*?)</div>', re.DOTALL)
chambre_re = re.compile(
	r'(?P<chambre>'
	r'Chambre\scommerciale\sfinancière\set\séconomique'
	r'|Chambre\scriminelle'
	r'|Chambre\ssociale'
	r'|Deuxième\schambre\scivile'
	r'|Première\schambre\scivile'
	r'|Première\sprésidence\s\(Ordonnance\)'
	r'|Troisième\schambre\scivile'
	r')', re.UNICODE
)

publication_re = re.compile(r"(?P<publication>Publié\sau.*?)\n")
formation_re = re.compile(r"(?P<formation>Formation restreinte.*?)\n")
ecli_re = re.compile(r"<p>(?P<ecli>ECLI:.*?)</p>") # TODO

# () : groupe
# (?P<ecli> ...) définit le groupe <ecli>. Permet de donner un nom permet de réutiliser le groupe just en l'appelant
# . : N'importe quel caractère
# * : caractère précédent répété 0 ou N fois.
# ? : O ou 1 caractère après ou après une étoile = mode frugal (non glouton) fait le check a chaque carctère puis avance d'un caractère si l'expression régulière n'est pas matchée
#  .compile : génère un automate 
# \s : caractère espace
# + : 1 ou N fois