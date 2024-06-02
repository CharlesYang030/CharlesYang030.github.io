---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 🙂 About Me
Hello! I'm Qihao (起豪), a second year master's student in the School of Computer Science at South China Normal Universty, advised by Professor [Tinyong Hao](https://scholar.google.com/citations?user=gM77jOQAAAAJ) and supported by the [TAM Lab](https://tony-hao.github.io/TAMLab/index.html). Here is my [CV](https://drive.google.com/file/d/15d8R2ZDqTyL0Aq-I79KFLRDP9mBv7cRX/view?usp=sharing).

My research interests include multimodal representation learning, natural language processing, multilingual lexical semantics, large language/vision-language models. See my Publications (mostly up to date) or [Google Scholar](https://scholar.google.com.hk/citations?user=rNsndk0AAAAJ) page for papers and more information.

I am a travel enthusiast. In the past two years, I have been to Shanghai, Hangzhou, Changsha, Xiangxi Tujia and Miao Autonomous Prefecture, Wuhan, Chaohu, Huangshan, Chengdu, Dujiangyan, Aba Tibetan Autonomous Prefecture, Tianjin, Beijing, Macau, Hong Kong, and Seoul. Traveling around the world is one of my dreams.

I am also one of the founders of LingX, an Empirical Linguistics Studio (语言学实证思辨坊) that aims to deliver consulting and methods related to quantitative linguistics and computational linguistics. The studio has designed and launched a course titled Text Mining and Python Programming and has organized online academic training sessions, attended by over 400 teachers and students from various universities. I am the principal instructor for the course.

Currently, I am pursuing a PhD opportunity for Fall 2025. I hope to further delve into research on practical multimodal applications, large multilingual/vision-language models.

# 🔥 News
- *2024.05.30*: &nbsp;🎉🎉 I will be joining [The Education University of Hong Kong](https://www.eduhk.hk/en/) as a 6-month research assistant from summer 2024, co-advised by Professor [Guandong Xu](https://repository.eduhk.hk/en/persons/guandong%E5%BE%90%E8%B2%AB%E6%9D%B1-xu). I would like to thank Professor Tianyong Hao for granting me the opportunity to go abroad for exchange!
- *2024.05.27*: &nbsp;🎉🎉 I am granted a project supported by the Scientific Research Innovation Project of Graduate School of South China Normal University. It earned me an honor!
- *2024.05.15*: &nbsp;🎉🎉 A paper is accepted by [ACL2024](https://2024.aclweb.org/) main conference! See you in Bangkok!
- *2024.04.15*: &nbsp;🎉🎉 I have arrived in Seoul, South Korea. And I am going to attend the [ICASSP2024](https://2024.ieeeicassp.org/) conference. Let's have a wonderful encounter!
- *2024.04.01*: &nbsp;🎉🎉 I pass the interview with the [TsinghuaNLP Lab](https://nlp.csai.tsinghua.edu.cn/) and establish a scientific research collaboration with the excellent researchers from Tsinghua University!

# 🎖 Honors and Awards
**Competition** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- [**First Prize**](https://drive.google.com/file/d/1Sqt36CK2VY11_ylk3TMVurHQL82B05jt/view?usp=sharing), International Natural Language Processing Competition SemEval-2023 Task 1 - Visual Word Sense Disambiguation (First Author)
- [**First Prize**](https://www.codabench.org/competitions/1970/), FigLang-2024 Shared Task - Multimodal Figurative Language (Second Author)

**Other** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- **First Prize**, Postgraduate Academic Forum of Guangdong-Hong Kong-Macao Greater Bay Area, 2023 
- **First Prize Scholarship**, South China Normal University, 2023
- **Third Prize**, Outstanding Paper Award, Computer Academy of Guangdong, 2023

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024 Main</div><img src='images/ACL2024_MODEL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PolCLIP: A Unified Image-Text Word Sense Disambiguation Model via Generating Multimodal Complementary Representations](https://openreview.net/forum?id=reddQnmur6)

**Qihao Yang**, Yong Li, Xuelin Wang, Fu Lee Wang (Hong Kong), Tianyong Hao*(corresponding author)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Word Sense Disambiguation, Contrastive Learning, Multimodal Learning.

**Project** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Supported by the Scientific Research Innovation Project of Graduate School of South China Normal University (Grant No. 2024KYLX090). 
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2024 Main</div><img src='images/ICASSP2024_MODEL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MTA: A Lightweight Multilingual Text Alignment Model for Cross-Language Visual Word Sense Disambiguation](https://ieeexplore.ieee.org/abstract/document/10447455)

**Qihao Yang**, Xuelin Wang, Yong Li, Lap-Kei Lee (Hong Kong), Fu Lee Wang (Hong Kong), Tianyong Hao*(corresponding author)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Visual Word Sense Disambiguation, Image-Text Retrieval, Multimodal Learning, Cross-lingual.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FigLang2024 (co-located with NAACL2024)</div><img src='images/FIGLANG2024_MODEL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FigCLIP: A Generative Multimodal Model with Bidirectional Cross-attention for Understanding Figurative Language via Visual Entailment](https://openreview.net/forum?id=AllykaUS7a)

**Qihao Yang**, Xuelin Wang*(corresponding author)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Multimodal Figurative Language, Vision-Language Model, Multimodal Representation Learning.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FigLang2024 (co-located with NAACL2024)</div><img src='images/FIGLANG2024_MODEL2.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A Textual Modal Supplement Framework for Understanding Multi-Modal Figurative Language](https://openreview.net/forum?id=rYLN8kMCYK)

Jiale Chen, **Qihao Yang**, Xuelian Dong, Xiaoling Mao, Tianyong Hao*(corresponding author)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Figurative Language, Vision-Language Model, Multimodal Fine-tune.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Artificial Intelligence in Medicine</div><img src='images/AIM_MODEL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Asymmetric Cross-modal Attention Network with Multimodal Augmented Mixup for Medical Visual Question Answering](https://www.sciencedirect.com/science/article/pii/S0933365723001811)

Yong Li, **Qihao Yang**, Fu Lee Wang (Hong Kong), Lap-Kei Lee (Hong Kong), Yingying Qu\*(corresponding author), Tianyong Hao\*(corresponding author)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Medical Visual Question Answering, Cross Modal Attention, Data Augmentation, Mixup, Multimodal Interaction.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ROCLING2023</div><img src='images/ROCLING_MODEL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LingX at ROCLING 2023 MultiNER-Health Task: Intelligent Capture of Chinese Medical Named Entities by LLMs](https://aclanthology.org/2023.rocling-1.44.pdf)

Xuelin Wang, **Qihao Yang***(corresponding author)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Medical Named Entity Recognition, Entity Extraction, Large Language Models.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SemEval2023 (co-located with ACL2023)</div><img src='images/SEMEVAL2023_MODEL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TAM of SCNU at SemEval-2023 Task 1: FCLL: A Fine-grained Contrastive Language-image Learning Model for Cross-language Visual Word Sense Disambiguation](https://aclanthology.org/2023.semeval-1.70)

**Qihao Yang***, Yong Li, Xuelin Wang, Shunhao Li, Tianyong Hao*(corresponding author)

(This paper won first prize in SemEval-2023 Task 1 competition, in which 57 teams participated. It earned me an honor and was a good start of my academic career!)

**Key words** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Visual Word Sense Disambiguation, Image-Text Retrieval, Contrastive Learning.
</div>
</div>
