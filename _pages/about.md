---
permalink: /
title: Chao Tang
---

## About Me {#about-me}

I am an undergraduate student in Automation at **Tongji University**, interested in building robots that can perceive, learn, and act in the physical world.

I explore learning-based locomotion and manipulation, connecting algorithms with robotic systems through simulation experiments and hands-on deployment.

## Research Interests {#research-interests}

I study how robots learn adaptable, generalizable skills — from adaptive training distributions for whole-body RL (nSGS) to fine-tuning VLA policies for real-robot manipulation — with humanoid robots as a long-term goal.

## Selected Projects {#selected-projects}

{% for project in site.data.projects %}
<article class="paper-box" id="project-{{ forloop.index }}">
  <figure class="paper-box-image">
    <picture class="project-animation">
      <source media="(prefers-reduced-motion: reduce)" srcset="{{ project.still | relative_url }}">
      <img src="{{ project.image | relative_url }}" alt="{{ project.alt }}" width="480" height="300" loading="lazy" title="{{ project.preview_note }}">
    </picture>
  </figure>
  <div class="paper-box-text">
    <h3>{{ project.title }}</h3>
    <p>{{ project.description }}</p>
    <p class="project-tech">{{ project.tech }}</p>
    <p class="project-links"><a href="{{ project.github }}">GitHub <span aria-hidden="true">↗</span></a><a href="{{ project.video | relative_url }}">Video <span aria-hidden="true">↗</span></a></p>
  </div>
</article>
{% endfor %}

## Research Experience {#research-experience}

<div class="experience-entry"><div><h3>AgiBot</h3><p>Mechanical Design Intern</p></div><span class="date">Summer 2026</span></div>

## Education {#education}

<div class="experience-entry"><div><h3>Tongji University</h3><p>B.Eng. in Automation (Excellence Program)</p></div><span class="date">2025 – 2029 (expected)</span></div>

## Beyond Research {#beyond-research}

<div class="music-note">
  <img class="music-photo" src="{{ "/images/music-gbc.jpg" | relative_url }}" width="4800" height="2511" alt="The Girls Band Cry band members together" loading="lazy">
  <div><span class="music-label">Music, off the clock</span><p>Beyond robotics, I love Yorushika and Girls Band Cry, especially Momoka Kawaragi. Music has always been part of my everyday life.</p></div>
</div>
