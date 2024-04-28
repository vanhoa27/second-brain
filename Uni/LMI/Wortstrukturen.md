---
tags:
  - uni/lmi
---
# Wortstrukturen

## Intuitiv
- $\mathcal W$ ist eine Wortstruktur
- W ist die Positionsmenge unsere Buchstaben
- $\leq$ wird verwendet um Reihenfolge/Ordnung der Buchstaben darzustellen
- s ist die Nachfolgerrelation
	- ist nicht *"zwingend"* notwendig (nützlich)
- $P_a$ ist eine einstellige Relation, um die Zugehörigkeit zu einem Buchstaben $a \in \Sigma$ darzustellen

## Formal
Sei $\Sigma$ ein Alphabet. Wir definieren die Signatur.
$$\sigma = \sigma(\Sigma) := \{\leq, s, (P_a)_{a \in \Sigma} \}$$
- **wobei**:
	- $\leq, s$ sind zweistellige Relationssymbole
	- $P_a$ ist ein einstelliges Relationssymbol
	
Zu $w = a_1, \dots, a_n \in \Sigma^*$ definieren wir die  *Wortstruktur*
$$\mathcal{W} = \mathcal{W} = (W,  \leq^{\mathcal{W}}, s^{\mathcal{W}}, (P_a^{W})_{a \in \Sigma})$$
- **wobei**:
	- $W = \{1, \dots, n\}$ ist die Menge der Positionen
	- $\leq^{W}$ ist die natürliche Ordnung auf $\{1,\dots, n\}$
	- $s^{W} := \{(i, i+1) : 1\leq i < n\}$ ist die Nachfolgerrelation
	- Für $a \in \Sigma$ gilt $P_a^W := \{i:a_i = a\}$