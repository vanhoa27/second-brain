---
tags:
  - logik
---
## gerichtete Graphen
- Weg der laenge $l$ in $\mathcal G$, $(v_0, \dots, v_l) \in V^{l+1}$ fuer ein $l \in \mathbb N$    
	- Abfolge von mit Kanten verbundenen Knoten
	- kann denselben Knoten *mehrmals* enthalten
	- kann **Zyklen** enthalten
- Pfad der laenge $l$ in $\mathcal G$, $(v_0, \dots, v_l) \in V^{l+1}$, sodass $v_i \neq v_j$ fuer alle $0 \leq i \leq j \leq l$
	- **Knoten** koennen nur max. einmal enthalten sein
		$\rightarrow$ keine Zyklen
- *geschlossener* Weg der laenge $l$ in $\mathcal G$, $(v_0, \dots, v_l) \in V^{l+1}$ mit $v_0 = v_l$
- Ein Kreis der laenge $l$ in $\mathcal G$ ist ein *geschlossener* Weg, $(v_0, \dots, v_l) \in V^{l+1}$, sodass $(v_1), \dots, (v_l)$ ein Pfad der laenge $l-1$ ist.
