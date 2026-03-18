# NatureLM-audio

```{raw} html
<script>
  (function() {
    var h1 = document.querySelector('.content h1');
    if (h1) {
      var badge = document.createElement('span');
      badge.className = 'version-badge';
      badge.textContent = 'v1.0';
      badge.style.marginLeft = '0.5rem';
      badge.style.verticalAlign = 'middle';
      badge.style.position = 'relative';
      badge.style.top = '2px';
      h1.appendChild(badge);
    }
  })();
</script>
```

```{toctree}
:maxdepth: 1
:caption: Getting Started
:hidden:

usage
```

```{toctree}
:maxdepth: 1
:caption: Demos & Examples
:hidden:

demo_video
examples
ui_demo
case_studies
```

```{toctree}
:maxdepth: 1
:caption: Reference
:hidden:

datasets
paper
```

<div class="resource-links">
  <a href="https://openreview.net/forum?id=hJVdwBpWjt" target="_blank" class="resource-link">
    <img src="_static/icons/paper.svg" class="resource-link-icon paper-icon" /> Paper
  </a>
  <span class="resource-link-sep">·</span>
  <a href="https://github.com/earthspecies/NatureLM-audio" target="_blank" rel="noopener" class="resource-link">
    <img src="_static/icons/github.svg" class="resource-link-icon github-icon" /> Code
  </a>
  <span class="resource-link-sep">·</span>
  <a href="https://huggingface.co/EarthSpeciesProject/NatureLM-audio" target="_blank" class="resource-link">
    <img src="_static/icons/hf-logo.svg" class="resource-link-icon" /> Model
  </a>
  <span class="resource-link-sep">·</span>
  <a href="https://huggingface.co/datasets/EarthSpeciesProject/BEANS-Zero" target="_blank" class="resource-link">
    <img src="_static/icons/hf-logo.svg" class="resource-link-icon" /> BEANS-Zero
  </a>
</div>

## Updates

```{raw} html
<div class="update-box">
  <span class="update-date">2025-05-27</span>
  We've updated NatureLM-audio with a flexible merge between the original Llama 3.1 8B and the LoRA fine-tuned weights. Merging with the original weights improves prompt flexibility but comes at the cost of some bioacoustic task performance. See the <a href="usage.html#model-merging">Usage</a> page and <a href="https://arxiv.org/abs/2511.05171" target="_blank">paper</a> for details.
</div>
```

## Overview

```{figure} _static/images/fig_architecture.png
:alt: NatureLM-audio architecture diagram
:width: 100%
:align: center
```

NatureLM-audio is the first audio-language foundation model designed specifically for bioacoustics. It combines a fine-tuned audio encoder ([BEATs](https://github.com/microsoft/unilm/tree/master/beats)) with a large language model ([Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)), enabling researchers to query bioacoustics data using natural language.

Key capabilities:

- **Flexible task support:** species classification, detection, call type and life stage classification, audio captioning, and individual counting
- **Zero-shot generalization:** trained across bioacoustics, speech, and music, the model transfers acoustic knowledge to unseen species and taxa
- **Real-world scale:** designed for large, diverse, and sparsely labeled datasets typical of conservation fieldwork
- **Accessible by design:** no task-specific fine-tuning required; researchers can interact with the model with plain English natural language prompts
