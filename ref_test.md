# Data science responsable et de confiance - Référentiel d'évaluation

### Restructuration en un référentiel d'évaluation de la maturité d'une organisation

On essaie ci-dessous de restructurer le référentiel d'évaluation, de manière à proposer un déroulé plus naturel, plus clair. L'enjeu est de faciliter l'exercice aux organisations souhaitant auto-évaluer le niveau de maturité de leur activité data science, par un meilleur guidage tout au long de l'évaluation.

L'évaluation est composée des 7 sections suivantes :

- [Section 1 - Protéger les données personnelles ou confidentielles](#section-1---protéger-les-données-personnelles-ou-confidentielles)
- [Section 2 - Prévenir les biais malencontreux](#section-2---prévenir-les-biais-malencontreux)
- [Section 3 - Evaluer la performance de manière rigoureuse](#section-3---evaluer-la-performance-de-manière-rigoureuse)
- [Section 4 - Etablir et maintenir une généalogie des modèles](#section-4---etablir-et-maintenir-une-généalogie-des-modèles)
- [Section 5 - Garantir la chaîne de responsabilité des modèles](#section-5---garantir-la-chaîne-de-responsabilité-des-modèles)
- [Section 6 - Utilisation de modèles prédictifs appris au sein de l'organisation](#section-6---utilisation-de-modèles-prédictifs-appris-au-sein-de-lorganisation)
- [Section 7 - Anticiper, suivre et minimiser les externalités de l'activité data science](#section-7---anticiper-suivre-et-minimiser-les-externalités-de-lactivité-data-science)

---

#### Section 1 - Protéger les données personnelles ou confidentielles

L'utilisation de données personnelles ou confidentielles fait porter le risque d'exposition de celles-ci, ce qui peut avoir des conséquences très préjudiciables pour les producteurs, gestionnaires, ou sujets de ces données. En particulier dans les projets de data science, elles doivent donc être protégées et les risques qu'elles fuitent ou soient exposées doivent être minimisés.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]  
[_[⇩ prochaine section](#section-2---prévenir-les-biais-malencontreux)_]

---

Q1.1 : **Législation et des exigences contractuelles applicables**  
En ce qui concerne les données personnelles et/ou confidentielles, les exigences légales, statutaires, réglementaires et contractuelles en vigueur et concernant votre organisation sont :

R1.1 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 1.1.a pas encore identifiées
- [ ] 1.1.b partiellement identifiées ou en cours d'identification
- [ ] 1.1.c identifiées
- [ ] 1.1.d identifiées et maîtrisées par les collaborateurs
- [ ] 1.1.e identifiées, documentées et maîtrisées par les collaborateurs

<details>
<summary>Expl1.1 :</summary>

Mettre en place des processus pour connaître et suivre l'évolution des réglementations applicables (très spécifiques dans certains secteurs), ainsi que pour documenter les approches et choix retenus pour être en conformité à chaque projet de data science. Exemple(s) intéressant(s) : [Welfare surveillance system violates human rights, Dutch court rules](https://www.theguardian.com/technology/2020/feb/05/welfare-surveillance-system-violates-human-rights-dutch-court-rules).

</details>

---

Q1.2 :  
Pour satisfaire à ces exigences, l’approche adoptée par votre organisation est :

R1.2 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 1.2.a informelle, basée sur la responsabilité et la compétence de chacun
- [ ] 1.2.b formalisée et accessible à tous les collaborateurs
- [ ] 1.2.c formalisée et maîtrisée par les collaborateurs
- [ ] 1.2.d formalisée, maîtrisée par les collaborateurs, documentée pour chaque traitement de données personnelles ou confidentielles

<details>
<summary>Expl1.2 :</summary>

Il s'agit de s'interroger sur la gestion des données personnelles ou confidentielles (stockage, accès, transfert, protection, responsabilités...), et de documenter les choix effectués.

</details>

---

Q1.3 : **Veille réglementaire**  
Un processus de veille réglementaire est-il mis en place, en interne ou via un prestataire spécialisé, pour connaître les évolutions applicables et impactantes pour votre organisation ?

R1.3 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 1.3.a nous ne faisons pas vraiment de veille réglementaire
- [ ] 1.3.b nous faisons une veille informelle, chaque collaborateur remonte les informations sur un moyen de communication dédiée
- [ ] 1.3.c nous avons une veille formalisée, les responsables sont identifiés, le processus est documenté

<details>
<summary>Expl1.3 :</summary>

Mettre en place des processus pour connaître et suivre l'évolution des réglementations applicables (très spécifiques dans certains secteurs), ainsi que pour documenter les approches et choix retenus pour être en conformité à chaque projet de data science. Exemple(s) intéressant(s) : [Welfare surveillance system violates human rights, Dutch court rules](https://www.theguardian.com/technology/2020/feb/05/welfare-surveillance-system-violates-human-rights-dutch-court-rules).

</details>

---

Q1.4 :  
La conformité de l'organisation aux exigences relatives aux données personnelles et confidentielles a-t-elle été auditée et est-elle reconnue par une certification, un organisme tiers ou équivalent ?

R1.4 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 1.4.a Oui
- [ ] 1.4.b Non

<details>
<summary>Expl1.4 :</summary>

Dans de nombreux secteurs il existe des exigences de conformité spécifiques. Il est généralement possible de formaliser la conformité d'une organisation par une certification ou un audit spécialisé, l'obtention d'un label.

</details>

---

Q1.5 : **Principe de minimisation**  
Dans le cadre des projets de data science, le principe de minimisation doit guider la collecte et l'utilisation de données personnelles ou confidentielles. Comment est-il mis en oeuvre au sein de votre organisation ?

R1.5 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 1.5.a Nous faisons en sorte de n'utiliser aucune données personnelles ou confidentielles. Nous ne sommes pas concernés par cet univers de risque
- [ ] 1.5.b Nous avons besoin d'en utiliser dans certains projets et le principe de minimisation est alors systématiquement appliqué
- [ ] 1.5.c Le principe de minimisation est connu des collaborateurs, qui l'appliquent en général
- [ ] 1.5.d Le réflexe "qui peut le plus peut le moins" vis-à-vis des données existe encore ici et là au sein de notre organisation. Dans certains projets, nous conservons des jeux de données beaucoup plus riches en données personnelles et confidentielles que ce qui est strictement utile au projet
  
---

_Les éléments suivants au sein de cette section ne s'appliquent qu'aux organisations n'ayant pas sélectionné la première réponse de R1.5. Les organisations non concernées sont donc invitées à passer à la [Section 2](#section-2-prévenir-les-biais-malencontreux)._

---

Q1.6 :  
_(Condition : R1.5 <> 1ère réponse)_  
Pour chaque traitement de données personnelles ou confidentielles nécessaire dans le cadre d'un projet de data science, au sein de votre organisation :

R1.6 :  
_(Type : réponses multiples possibles)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation)_

- [ ] 1.6.a nous élaborons un _Privacy Impact Assessment_ (PIA)
- [ ] 1.6.b nous mettons en oeuvre des mesures de protections (concernant notamment le transfert, le stockage, et l'accès aux données concernées)
- [ ] 1.6.c nous documentons les PIA et mesures mises en oeuvre et nous les conservons au sein des projets
- [ ] 1.6.d nous contractualisons les relations avec les fournisseurs et les clients et les responsabilités qui en découlent

---

Q1.7 : **Sécurité de l'apprentissage automatique et _PETs_ - Niveau de connaissance**  
_(Condition : R1.5 <> 1ère réponse)_  
La sécurité de l'apprentissage automatique (_ML security_) est un domaine en plein développement. Dans certains cas de figure, les modèles prédictifs appris sur des données confidentielles peuvent révéler des éléments de ces données confidentielles. Au sein de votre organisation, au sujet des vulnérabilités liées aux modèles de ML et aux _Privacy Enhancing Technologies (PETs)_, le niveau de connaissance générale des collaborateurs intervant sur les projets de data science est :

R1.7 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 1.7.a Débutant
- [ ] 1.7.b Intermédiaire
- [ ] 1.7.c Confirmé
- [ ] 1.7.d Expert

<details>
<summary>Expl1.7 :</summary>

L'état de l'art de la sécurité du ML est en constante évolution. S'il est impossible de se prémunir contre toutes les vulnérabilités à tout instant, il est crucial de s'en préoccuper et se tenir au courant.
Référence(s) intéressante(s) :

- [OWASP Top Five ML risks](https://github.com/OWASP/Top-5-Machine-Learning-Risks/blob/master/Top%205%20Machine%20Learning%20Risks.md)
- [The secret-sharer: evaluating and testing unintended memorization in neural networks](https://blog.acolyer.org/2019/09/23/the-secret-sharer/)
- [Inverting Gradients - How easy is it to break privacy in federated learning?](https://arxiv.org/abs/2003.14053)

</details>

---

Q1.8 : **Sécurité de l'apprentissage automatique et _PETs_ - Mise en oeuvre**  
_(Condition : R1.5 <> 1ère réponse)_  
Toujours au sujet des vulnérabilités liées aux modèles de ML et aux _(PETs)_ :

R1.8 :  
_(Type : réponses multiples possibles)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation)_

- [ ] 1.8.a Une veille technique est mise en oeuvre
- [ ] 1.8.b Les collaborateurs reçoivent régulièrement des informations / formations qui leur permettent de monter en compétences
- [ ] 1.8.c Dans certains projets, nous mettons en oeuvre des _PETs_ permettant de réduire les risques liés aux modèles que nous élaborons
- [ ] 1.8.d Sur chaque projet, les vulnérabilités qui s'y appliquent et les _PETs_ mises en oeuvre sont documentées dans la Généalogie de Bout-en-Bout (G2B) de chaque modèle

<details>
<summary>Expl1.8 :</summary>

L'état de l'art de la sécurité du ML est en constante évolution. S'il est impossible de se prémunir contre toutes les vulnérabilités à tout instant, il est crucial de s'en préoccuper et se tenir au courant.
Référence(s) intéressante(s) :

- [OWASP Top Five ML risks](https://github.com/OWASP/Top-5-Machine-Learning-Risks/blob/master/Top%205%20Machine%20Learning%20Risks.md)
- [The secret-sharer: evaluating and testing unintended memorization in neural networks](https://blog.acolyer.org/2019/09/23/the-secret-sharer/)
- [Inverting Gradients - How easy is it to break privacy in federated learning?](https://arxiv.org/abs/2003.14053)

Selon les niveaux de risque et de sensibilité des projets, certaines approches _PETs_ seront sélectionnées et implémentées. Il est important de suivre l'évolution de l'état de l'art et des pratiques, et de documenter les choix réalisés. On introduit ici la notion de ["généalogie de bout-en-bout"](#section-4---etablir-et-maintenir-une-généalogie-des-modèles).

</details>

---

Q1.9 : **Notifications d’incidents de sécurité aux autorités de régulation**  
_(Condition : R1.5 <> 1ère réponse)_  
Dans le cas de figure où un modèle que l'organisation a élaboré est utilisé ou accessible par une(des) partie(s) prenante(s) externe(s), et qu'une vulnérabilité nouvelle est publiée, présente un risque de s'y appliquer et crée ainsi un risque d'exposition de données personnelles ou confidentielles :

R1.9 :  
_(Type : réponses multiples possibles)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation)_

- [ ] 1.9.a Nous avons une procédure décrivant la marche à suivre
- [ ] 1.9.b Notre procédure inclut une communication aux parties prenantes en question
- [ ] 1.9.c Notre procédure référence les autorités auxquelles nous devons faire un signalement

<details>
<summary>Expl1.9 :</summary>

Il existe dans certains secteurs des obligations de signalement des incidents de sécurité aux autorités de régulation (e.g. CNIL, ANSSI, ARS...). Référence intéressante : [Notifications d’incidents de sécurité aux autorités de régulation : comment s’organiser et à qui s’adresser ?](https://www.cnil.fr/fr/notifications-dincidents-de-securite-aux-autorites-de-regulation-comment-sorganiser-et-qui-sadresser) sur le site de la CNIL.

</details>

---
---

#### Section 2 - Prévenir les biais malencontreux

L'utilisation de modèles prédictifs élaborés à partir de données historiques peut se révéler contre-productive lorsque les données historiques sont contaminées par des phénomènes problématiques (e.g. qualité de certains points de données, données non comparables, phénomène social non souhaitable du fait de l'époque...). Il apparaît indispensable de s'interroger sur ce risque et d'étudier la nature des données utilisées, les conditions dans lesquelles elles ont été produites et assembées, et ce qu'elles représentent.
Dans certains cas, une spécification de l'équité recherchée entre populations doit également être définie. L'équité d'un modèle peut [être définie de plusieurs manières qui peuvent être incompatibles entre elles](https://papers.nips.cc/paper/6995-counterfactual-fairness), et l'interprétation de scores de performances doit donc se faire dans le cadre de l'une de ces définitions.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]  
[_[⇩ prochaine section](#section-3---evaluer-la-performance-de-manière-rigoureuse)_]

---

Q2.1 : **Analyse des données d'entraînement utilisées**  
Au sein des projets de data science et lors de l'élaboration de jeux de données d'entraînement, un travail de réflexion et recherche de phénomènes intempestifs ou parasites du fait de l'époque, du contexte, des outils ou processus d'enregistrement peut s'avérer crucial pour prévenir des biais malencontreux. Votre organisation :

R2.1 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 2.1.a fonctionne de manière informelle à ce sujet et s'appuie sur la compétence et la responsabilité des collaborateurs impliquées
- [ ] 2.1.b dispose d'une approche documentée et systématiquement mise en oeuvre

<details>
<summary>Expl2.1 :</summary>

Il s'agit de s'obliger à s'interroger sur ces sujets et donc à réfléchir aux données utilisées, la manière dont elles ont été produites etc.
Référence intéressante :

- [Tour of Data Sampling Methods for Imbalanced Classification](https://machinelearningmastery.com/data-sampling-methods-for-imbalanced-classification/)

</details>

---

Q2.2 :
Votre organisation est-elle concernée par des cas de figure où les modèles prédictifs sont utilisés dans des environnements thématiques où il y a des risques de discrimination à l'encontre de certains groupes sociaux (genre, origine, âge, etc.) ?

R2.2 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 2.2.a Concerné
- [ ] 2.2.b Non concerné

---

_Les éléments suivants au sein de cette section ne s'appliquent qu'aux organisations ayant sélectionné la réponse "Concerné" de R2.2. Les organisations non concernées sont donc invitées à passer à la [Section 3](#section-3-evaluer-la-performance-de-manière-rigoureuse)._

---

Q2.3 : **Prévention des biais discriminatoires**  
_(Condition : R2.2 = Concerné)_  
Dans les cas de figure où les modèles prédictifs que votre organisation élabore sont utilisés dans des environnements thématiques où il y a des risques de discrimination à l'encontre de certains groupes sociaux (genre, origine, âge, etc.) :

R2.3 :  
_(Type : réponses multiples possibles)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation)_

- [ ] 2.3.a Nous portons une attention particulière à l'identification de variables protégées et à leurs proxys éventuels
- [ ] 2.3.b Nous procédons à des évaluations sur des données de test comprenant différentes sous-populations afin d'identifier les éventuels biais problématiques
- [ ] 2.3.c Nous sélectionnons et mettons en oeuvre une ou plusieurs mesure(s) de justice et d'équité (_fairness metric_)
- [ ] 2.3.d Nous mettons en oeuvre des approches de type _data augmentation_ ou _re-weighting_
- [ ] 2.3.e Les pratiques ci-dessus que nous mettons en oeuvre sont dûment documentées intégrées à la G2B des modèles concernés

<details>
<summary>Expl2.3 :</summary>

Il s'agit de s'interroger systématiquement, à chaque projet de data science et selon l'objectif et l'usage cible du modèle que l'on veut élaborer, sur les features pouvant directement ou indirectement être à l'origine d'un risque de biais discriminatoire.
Compléments et références intéressantes :

- _fairness metrics_ : _[counterfactual fairness](https://papers.nips.cc/paper/6995-counterfactual-fairness)_, _[adversarial debiaising](https://arxiv.org/pdf/1801.07593.pdf)_
- utilisation de données synthétiques, _data augmentation_, _re-weighting_ : lorsque de telles techniques sont utilisées il est important de les expliciter, au risque sinon de perdre de l'information sur la manière dont un modèle a été élaboré.

</details>

---
---

#### Section 3 - Evaluer la performance de manière rigoureuse

Le score de performance d'un modèle prédictif est déterminant pour son adoption dans des produits, systèmes ou processus. L'évaluation de la performance se doit donc d'être rigoureuse. Par ailleurs un modèle prédictif peut-être utilisé comme un système automatique, dont les règles de fonctionnement ne sont pas écrites _in extenso_ et ne se prêtent pas ou mal à être explicitées, débattues, ajustées. Des efforts sont donc nécessaires sur l'interprétation et l'explication des choix réalisés à l'aide de ces systèmes.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]  
[_[⇩ prochaine section](#section-4---etablir-et-maintenir-une-généalogie-des-modèles)_]

---

Q3.1 : **Séparation des jeux de données de test**  
Au sein des projets de data science et lors de l'élaboration de jeux de données de test, il est capital d'assurer la non-contamination par des données d'entraînement. Votre organisation :

R3.1 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 3.1.a fonctionne de manière informelle à ce sujet et s'appuie sur la compétence et la responsabilité des collaborateurs impliquées
- [ ] 3.1.b dispose d'une approche documentée et systématiquement mise en oeuvre d'isolation des testsets
- [ ] 3.1.c utilise un outil de versionnage et de traçabilité des jeux de données d'entraînement et de test utilisés, permettant ainsi de vérifier ou auditer ultérieurement la non-contamination des données de tests
- [ ] 3.1.d prévoit systématiquement l'élaboration de deux testsets ou plus pour gagner en résilience

---

Q3.2: **Projets d'apprentissage distribué préservant la confidentialité**  
Dans les cas de figure de projets de data science basé sur l'apprentissage distribué ou fédéré (_distributed learning_ ou _federated learning_) sur des jeux de données multiples et dont la confidentialité doit être préservée vis-à-vis des autres (_privacy-preserving_) :

R3.2:  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 3.2.a Nous ne participons pas à des projets de _privacy-preserving distributed learning_ | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 3.2.b Nous maîtrisons et mettons en oeuvre des approches permettant d'élaborer des jeux de données de test de manière à ce qu'il n'y ait pas de contamination croisée entre données d'entraînement et de test provenant des différents partenaires
- [ ] 3.2.c À ce stade nous ne maîtrisons pas les méthodes permettant d'élaborer des jeux de données de test de manière à ce qu'il n'y ait pas de contamination croisée entre données d'entraînement et de test provenant des différents partenaires

---

Q3.3 : **Analyse des données de test**  
Au sein des projets de data science et lors de l'élaboration de jeux de données de test, un travail de réflexion et recherche de phénomènes intempestifs ou parasites du fait de l'époque, du contexte, des outils ou processus d'enregistrement peut s'avérer crucial pour la signification des scores de performance. Votre organisation :

R3.3 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 3.3.a fonctionne de manière informelle à ce sujet et s'appuie sur la compétence et la responsabilité des collaborateurs impliquées
- [ ] 3.3.b dispose d'une approche documentée et systématiquement mise en oeuvre

<details>
<summary>Expl3.3 :</summary>

L'utilisation de modèles prédictifs testés sur des données historiques peut se révéler contre-productive lorsque les données historiques en question sont contaminées par des phénomènes problématiques (e.g. qualité de certains points de données, données non comparables, phénomène social non souhaitable du fait de l'époque...). Il apparaît indispensable de s'interroger sur ce risque et d'étudier la nature des données utilisées, les conditions dans lesquelles elles ont été produites et assembées, et ce qu'elles représentent.

</details>

---

Q3.4 : **Validation des performances**  
Votre organisation met-elle en oeuvre les approches suivantes :

R3.4 :  
_(Type : réponses multiples possibles)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation)_

- [ ] 3.4.a Choix d'une métrique de performance en amont de l'apprentissage machine, parmi les métriques les plus standards possibles
- [ ] 3.4.b La mise en oeuvre de mesures de robustesse (_robustness metrics_) est considérée et évaluée pour chaque projet d'élaboration d'un modèle, et systématiquement mise en oeuvre au sein des projets où les données d'entrées peuvent être soumises à des perturbations fines (e.g. images, sons)
- [ ] 3.4.c Les pratiques ci-dessus que nous mettons en oeuvre sont dûment documentées intégrées à la [G2B](#section-4---etablir-et-maintenir-une-généalogie-des-modèles) des modèles concernés

<details>
<summary>Expl3.4 :</summary>

Références intéressantes :

- _[p-hacking, data dredging](https://fr.wikipedia.org/wiki/Data_dredging)_
- _robustness metrics_ : _[noise sensitivity score](https://arxiv.org/abs/1806.01477)_.

</details>

---

Q3.5 : **Suivi de la performance dans le temps**  
Dans les cas de figure où des modèles prédictifs élaborés par votre organisation sont utilisés dans des systèmes en production :

R3.5 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 3.5.a Les modèles que nous élaborons ne sont pas utilisés actuellement | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 3.5.b La performance est systématiquement ré-évaluée lorsque le modèle est mis à jour
- [ ] 3.5.c La performance est systématiquement ré-évaluée lorsque le contexte d'utilisation du modèle évolue, ce qui peut créer un risque sur la performance du modèle du fait de l'évolution de l'espace des données d'entrée
- [ ] 3.5.d La performance est ré-évaluée régulièrement sur des données de test actualisée, car les données d'entrées peuvent évoluer (exemple : une variable qui ne serait plus renseignée à la même fréquence qu'avant par les utilisateurs dans un SI)
- [ ] 3.5.e Des contrôles aléatoires sont réalisés sur des prédictions afin d'en contrôler la cohérence

<details>
<summary>Expl3.5 :</summary>

Même sur un modèle stable il existe un risque que les données d'entrée ne soient plus dans le domaine au bout d'un certain temps (population & distribution), exemple : une variable qui ne serait plus renseignée à la même fréquence qu'avant par les utilisateurs dans un SI. Il est donc nécessaire de contrôler régulièrement la performance d'un modèle utilisé dans son contexte d'utilisation.
Référence intéressante :

- [Continuous delivery for machine learning](https://martinfowler.com/articles/cd4ml.html)

</details>

---

Q3.6 : **Seuils de classification et plages d'indécision**  
Lors de l'élaboration d'un modèle de classification, pour la définition des seuils de classification, votre organisation :

R3.6 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 3.6.a fonctionne de manière informelle à ce sujet et s'appuie sur la compétence et la responsabilité des collaborateurs impliquées
- [ ] 3.6.b dispose d'une approche documentée et systématiquement mise en oeuvre
- [ ] 3.6.c dispose d'une approche documentée et systématiquement mise en oeuvre, qui inclut la possibilité de maintenir des plages d'indécision
- [ ] 3.6.d les choix réalisés pour chaque modèle et mis en oeuvre sont dûment documentées intégrées à la G2B des modèles concernés

<details>
<summary>Expl3.6 :</summary>

Référence intéressante :

- [Opening the algorithm’s black box and understand its outputs](https://medium.com/@asaboni/opening-the-algorithms-black-box-and-understand-its-outputs-e2363b0a887c)

</details>

---

Q3.7 : **Explicabilité et interprétabilité**  
Au sein des projets de data science qui visent à élaborer des modèles prédictifs en vue d'être utilisés en inférence :

R3.7 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 3.7.a Notre organisation n'est pour l'instant pas familière avec les méthodes et outils d'explicabilité et d'interprétabilité des modèles
- [ ] 3.7.b Nous nous intéressons au sujet de l'explicabilité et l'interprétabilité des modèles et dialoguons avec nos parties prenantes, mais nous ne mettons pas en oeuvre d'approche de ce type à ce stade
- [ ] 3.7.c Nous faisons en sorte que les modèles que nous élaborons fournissent lorsque cela est pertinent a minima un niveau de confiance dans les prédictions réalisées
- [ ] 3.7.d Nous mettons en oeuvre des approches avancées pour l'explicabilité et l'interprétabilité des modèles

<details>
<summary>Expl3.7 :</summary>

Référence intéressante :

- [La confiance des utilisateurs dans les systèmes impliquant de l’Intelligence Artificielle](https://blog.octo.com/la-confiance-des-utilisateurs-dans-les-systemes-impliquant-de-lintelligence-artificielle/)

</details>

---
---

#### Section 4 - Etablir et maintenir une généalogie des modèles

Un modèle prédictif est un objet informatique complexe qui peut évoluer au fil des apprentissages. Tracer les étapes de son élaboration et de son évolution permet d'en constituer une forme de **généalogie**, pré-requis pour **reproduire ou auditer** un modèle.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]  
[_[⇩ prochaine section](#section-5---garantir-la-chaîne-de-responsabilité-des-modèles)_]

---

Q4.1 : **"Généalogie de bout-en-bout" des modèles**  
Une généalogie de bout-en-bout (G2B) des modèles est alimentée et tenue à jour dans le cadre des projets de data science, tout au long des phase de collecte de données, conception, entraînement, validation et exploitation :

R4.1 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 4.1.a À ce stade nous n'avons pas mis en oeuvre d'approche de ce type
- [ ] 4.1.b Ces informations existent et sont enregistrées afin de ne pas être perdues, mais elles peuvent l'être de manière désordonnée et ne sont pas versionnées
- [ ] 4.1.c Elles sont rassemblées en un unique document qui accompagne systématiquement le modèle
- [ ] 4.1.d Elles sont rassemblées en un unique document qui accompagne systématiquement le modèle et versionnées

<details>
<summary>Expl4.1 :</summary>

Ce concept de "généalogie de bout-en-bout" d'un modèle peut se décliner sous la forme  par exemple d'un document de référence reprenant tous les choix importants ainsi que tout l'historique d'élaboration du modèle, et de processus internes organisant cette activité.

</details>

---

Q4.2 : **Conditions et limites d'utilisation d'un modèle**  
Dans le cadre des projets de data science, les "conditions et limites de validité" d'un modèle conçu, entraîné et validé par l'organisation :

R4.2 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 4.2.a ne sont pas documentées | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 4.2.b sont explicitées et documentées
- [ ] 4.2.c sont versionnées
- [ ] 4.2.d les documents présentant ces "conditions et limites de validité" accompagnent systématiquement les modèles tout au long de leur cycle de vie

<details>
<summary>Expl4.2 :</summary>

Il s'agit d'expliciter et d'adjoindre au modèle la description du contexte d'utilisation pour lequel il a été conçu et dans lequel sa performance annoncée est significative. Ce concept de "conditions et limites de validité" peut se décliner sous la forme d'un document synthétique ou d'une section spécifique dans la "généalogie de bout-en-bout".

</details>

---
---

#### Section 5 - Garantir la chaîne de responsabilité des modèles

Utiliser des systèmes automatiques basés sur des modèles dont les règles ont été "apprises" (et non définies et formalisées) interroge le fonctionnement des organisations. Il apparaît indispensable de garantir une chaîne de responsabilité claire, de personnes physiques ou morales, pour chaque modèle.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]  
[_[⇩ prochaine section](#section-6---utilisation-de-modèles-prédictifs-appris-au-sein-de-lorganisation)_]

---

Q5.1 : **Chaîne de valeur et de responsabilités**  
Dans le cas de figure des projets de data science où plusieurs acteurs, y compris internes à l'organisation (équipes, départements, filiales), sont parties prenantes tout au long de la chaîne de valeur et de responsabilités :

R5.1 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 5.1.a Au sein de notre organisation les projets de data science sont menés de bout-en-bout par des équipes autonomes, y compris l'élaboration de jeux de données et l'exploitation pour son propre compte des modèles. En conséquence, pour chaque projet une équipe autonome est seule responsable | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 5.1.b Nous procédons systématiquement à l'identification des risques et responsabilités de chacune des parties prenantes internes ou externes avec lesquelles nous collaborons
- [ ] 5.1.c Nous contractualisons systématiquement avec les acteurs amont (e.g. fournisseurs de données) et aval (e.g. utilisateurs de modèles)

<details>
<summary>Expl5.1 :</summary>

Il est important de s'assurer que les organisations en amont et en aval de la chaîne identifient et endossent bien leurs responsabilités sur leurs segments de la chaîne de valeur.

</details>

---

Q5.2 : **Répartition de la création de valeur**  
Dans les cas de figure des projets de data science où plusieurs partenaires concourent aux côtés de votre organisation à l'élaboration d'un modèle, et que celui-ci est ou sera l'objet d'une activité économique :

R5.2 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 5.2.a Notre organisation exerce ses activités de data science de manière autonome, y compris l'élaboration de jeux de données et l'exploitation pour son propre compte des modèles. Elle n'est donc pas concernée  | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 5.2.b À ce stade nous n'avons pas structuré cet aspect des projets de data science multi-partenaires | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 5.2.c Dans ces cas de figure nous contractualisons le volet économique de la relation avec les parties prenantes impliquées en amont du projet
- [ ] 5.2.d Notre organisation s'est dotée d'une politique encadrant de manière responsable le partage de valeur avec les parties prenantes impliquées

<details>
<summary>Expl5.2 :</summary>

Lorsque plusieurs partenaires collaborent pour l'élaboration d'un modèle, il est important que la répartition de valeur consécutives à une activité économique dans laquelle le modèle joue un rôle soit explicitée et contractualisée. Dans certains cas de figure cette question peut être complexe, par exemple lorsqu'un modèle est entraîné de manière distribuée sur plusieurs jeux de données.
Référence intéressante :

- [Exploration of dataset contributivity to a model in collaborative ML projects](https://github.com/SubstraFoundation/distributed-learning-contributivity)

</details>

---

Q5.3 : **Sous-traitance**  
Les activités sous-traitées auprès ou en partenariat avec une organisation tierce sont soumises aux mêmes exigences que celles que votre organisation s'applique :

R5.3 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 5.3.a Oui
- [ ] 5.3.b Non

<details>
<summary>Expl5.3 :</summary>

Comme dans les cadres connues du management des SI (ISO 27001) ou du RGPD, il est important de ne pas diluer les responsabilités dans des chaînes de sous-traitance non maîtrisées.

</details>

---

#### Section 6 - Utilisation de modèles prédictifs appris au sein de l'organisation

Utiliser des systèmes automatiques basés sur des modèles dont les règles ont été "apprises" (et non définies et formalisées) interroge le fonctionnement des organisations. Il est important de préserver la capacité de réaction et la résilience de l'organisation, notamment pour traiter les cas de figure où les modèles prédictifs auront été à l'origine d'un résultat non souhaitable pour l'organisation et ses parties prenantes.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]  
[_[⇩ prochaine section](#section-7---anticiper-suivre-et-minimiser-les-externalités-de-lactivité-data-science)_]

---

Q6.1 : **Usage des modèles dans les conditions pour lesquelles ils ont été élaborés**  
Si votre organisation utilise pour son propre compte des modèles prédictifs :

R6.1 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 6.1.a Notre organisation n'utilise pas de modèles prédicifs élaboré par apprentissage automatique pour son propre compte | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 6.1.b **Un registre des modèles prédictifs** identifie tous les modèles utilisés par l'organisation, nous le maintenons à jour
- [ ] 6.1.c Pour chaque modèle nous disposons d'un **responsable point de contact** défini, identifiable et contactable simplement
- [ ] 6.1.d Pour chaque modèle, nous réalisons systématiquement une **évaluation des risques** consécutifs à d'éventuels, incidents, défaillances, biais
- [ ] 6.1.e Pour chaque modèle, nous définissons et testons une procédure de suspension du modèle et un mode de fonctionnement dégradé sans le modèle, pour parer au cas de figure où le modèle serait sujet à une défaillance ou un comportement anormal
- [ ] 6.1.f Pour chaque modèle, nous étudions sa [G2B](#section-4---etablir-et-maintenir-une-généalogie-des-modèles) et ses conditions et limites d'utilisation pour comprendre le modèle avant de l'utiliser
- [ ] 6.1.g Nous utilisons toujours les modèles pour des **usages en adéquation avec leurs conditions et limites d'utilisation**

<details>
<summary>Expl6.1 :</summary>

Utiliser des systèmes automatiques basés sur des modèles dont les règles ont été "apprises" (et non définies et formalisées) interroge le fonctionnement des organisations. Il est important d'évaluer les conséquences et les réactions en cas d'incident. Par ailleurs il est important qu'une personne responsable soit clairement identifiée de manière à ne laisser aucune partie prenante démunie face à une conséquence inattendue ou inappropriée. Enfin il est important de s'interroger sur les "conditions et limites de validité" des modèles que l'on utilise afin de s'assurer que l'usage que l'on prévoit est bien en adéquation.

</details>

---

Q6.2 : **Gestion des prédictions problématiques, processus de contournement, _human agency_**  
Les systèmes automatiques, en particulier lorsqu'ils s'appuient sur des modèles prédictifs appris, sont utilisés en production pour gagner en efficacité. Il se trouve que par nature, ils génèrent de temps en temps des résultats non souhaitables pour l'organisation et ses parties prenantes (e.g. prédiction erronée), puisqu'ils ne généraliseront jamais une performance de 100%.

R6.2 :  
_(Type : combiné)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation. Attention, certaines combinaisons ne seraient pas cohérentes)_

- [ ] 6.2.a Notre organisation n'utilise pas de modèles prédicifs élaboré par apprentissage automatique pour son propre compte | _(Lorsque cette réponse est sélectionnée, les autres ne peuvent pas l'être)_
- [ ] 6.2.b Nous intégrons dans les systèmes automatiques s'appuyant sur des modèles prédictifs appris les fonctionnalités permettant de gérer ces cas de résultats non souhaitables. Cela est fait selon une modalité de gestion d'incident, c'est-à-dire de correction _ex post_ du résultat non souhaitable
- [ ] 6.2.c Nous intégrons dans les systèmes automatiques s'appuyant sur des modèles prédictifs appris les fonctionnalités permettant de gérer ces cas de résultats non souhaitables. Cela est fait _ex ante_, en sollicitant un opérateur humain dans un certain nombre de cas où l'intervalle de confiance pour la décision automatique n'est pas satisfaisant
- [ ] 6.2.d Nous mettons en place des mécanismes permettant à un opérateur humain, dans certaines conditions définies, d'aller contre une décision d'un modèle s'il identifie que le modèle commet une erreur

<details>
<summary>Expl6.2 :</summary>

Utiliser des systèmes automatiques basés sur des modèles dont les règles ont été "apprises" (et non définies et formalisées) interroge le fonctionnement des organisations. Il est important de préserver la capacité de réaction et la résilience de l'organisation.

</details>

---

#### Section 7 - Anticiper, suivre et minimiser les externalités de l'activité data science

La mise en place d'un système automatique basé sur un modèle prédictif peut générer des externalités négatives sociales et environnementales. En prendre conscience est indispensable, ainsi qu'anticiper, chercher à suivre et minimiser les différents impacts négatifs.

[_[⇧ retour à la liste des sections](#restructuration-en-un-référentiel-dévaluation-de-la-maturité-dune-organisation)_]

---

Q7.1 : **Impact CO2**  
Au sujet de l'impact CO2 de son activité data science, au sein de votre organisation :

R7.1 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 7.1.a À ce stade nous ne nous sommes pas penchés sur l'impact CO2 de notre activité data science ou de nos modèles prédictifs
- [ ] 7.1.b Nous avons défini des indicateurs pour savoir quoi mesurer précisément
- [ ] 7.1.c Nous avons défini des indicateurs et nous incluons leurs mesures dans les G2B des modèles
- [ ] 7.1.d Nous avons défini des indicateurs et nous les suivons régulièrement
- [ ] 7.1.e Nous avons défini des indicateurs, nous les suivons régulièrement, et nous nous sommes fixés des objectifs d'amélioration

<details>
<summary>Expl7.1 :</summary>

Il est important de s'interroger et de conscientiser les coûts environnementaux. Référence(s) intéressante(s) :

- [ML Impact Calculator](https://mlco2.github.io/impact/)

</details>

---

Q7.2 : **Impact social**  
Dans certains cas, la mise en place d'un système automatique basé sur un modèle prédictif peut générer des externalités négatives sur les parties prenantes amont (par exemple annotation de données), et sur les parties prenantes aval (par exemple automatisation de certains postes). Lors de chaque projet d'élaboration ou d'utilisation d'un modèle prédictif, votre organisation :

R7.2 :  
_(Type : réponse unique)_  
_(Sélectionner une seule réponse, correspondant le mieux au niveau de maturité de l'organisation sur ce sujet)_

- [ ] 7.2.a À ce stade nous ne nous penchons pas sur l'impact social de notre activité data science ou de nos modèles prédictifs
- [ ] 7.2.b Dans certains cas nous nous interrogeons sur l'impact social
- [ ] 7.2.c Nous menons ce travail de réflexion sur l'impact social à chaque projet
- [ ] 7.2.d Nous menons ce travail de réflexion sur l'impact social à chaque projet et l'impact social est documenté dans la G2B de chaque modèle
- [ ] 7.2.e Nous menons ce travail de réflexion sur l'impact social à chaque projet, l'impact social est documenté dans la G2B de chaque modèle, et nous entamons systématiquement un dialogue avec les parties prenantes concernées amont et aval

<details>
<summary>Expl7.2 :</summary>

Il est important de s'interroger et d'échanger avec ses parties prenantes. Cela vaut tant pour l'aval (e.g. automatisation de certains emplois) que pour l'amont (e.g. tâches d'annotations de données parfois d'une très grande violence).

</details>

---

Q7.3 : **Ethique et non-malfaisance**  
Au sein de votre organisation :

R7.3 :  
_(Type : réponses multiples possibles)_  
_(Sélectionner tous les éléments de réponse correspondant à des pratiques de votre organisation)_

- [ ] 7.3.a Les collaborateurs concernés par les activités data science reçoivent une formation à l'éthique
- [ ] 7.3.b Notre organisation s'est dotée d'une politique en matière d'éthique

<details>
<summary>Expl7.3 :</summary>

Travailler sur de grands volumes de données dont certaines peuvent être sensibles, utiliser des systèmes automatiques basés sur des modèles dont les règles ont été "apprises" (et non définies et formalisées) interrogent le fonctionnement des organisations et la responsabilité individuelle de chacun. Il est important que l'organisation s'assure que les enjeux éthiques ne sont pas inconnus de son personnel.
Référence intéressante :

- Rapport [Éthique et responsabilité des algorithmes publics](https://www.etalab.gouv.fr/wp-content/uploads/2020/01/Rapport-ENA-Ethique-et-responsabilit%C3%A9-des-algorithmes-publics.pdf), Etalab / ENA, Janvier 2020
- [Déclaration de Montréal pour l'IA responsable](https://www.declarationmontreal-iaresponsable.com/la-declaration)
- [Serment Holberton-Turing](https://www.holbertonturingoath.org/accueil)
- [Serment d'Hippocrate pour data scientist](https://dataforgood.fr/projects/4_serment-hippocrate.html)
- [Future of Life's AI principles](https://futureoflife.org/ai-principles/)

</details>

---
