---
name: doc-coauthoring
description: >
  Guide users through structured workflow for co-authoring documentation.
  Use when: (1) writing documentation or proposals, (2) creating technical specs,
  (3) drafting decision documents, (4) collaborative content creation.
  Triggers: "write docs", "create proposal", "draft spec", "decision doc",
  "technical documentation", "help me write", "coauthor", "document together".
---

# Document Co-authoring Workflow

Structured workflow for efficiently co-authoring documentation, proposals, technical specs, and decision documents.

## Overview

This workflow helps you:
1. Transfer context efficiently to Claude
2. Iterate and refine content together
3. Verify the document works for readers
4. Produce polished final output

## Phase 1: Context Transfer

### What to Share
```markdown
## Document Purpose
- What is this document?
- Who is the audience?
- What decision/action should result?

## Key Points to Cover
1. [Main point 1]
2. [Main point 2]
3. [Main point 3]

## Constraints
- Length: [word count / page limit]
- Format: [memo / proposal / spec / etc.]
- Tone: [formal / casual / technical]

## Existing Materials
- [Links or paste relevant context]
- [Previous versions if updating]
- [Related documents]

## Must Include
- [Required section 1]
- [Required section 2]

## Must Avoid
- [Topic to avoid]
- [Perspective to avoid]
```

### Quick Context Template
```
I need to write a [TYPE] for [AUDIENCE].
Goal: [WHAT SHOULD HAPPEN AFTER READING]
Key message: [CORE POINT]
Constraints: [LENGTH/FORMAT/TONE]
Include: [MUST-HAVES]
```

## Phase 2: Outline Development

### Request Outline First
```
Based on the context, create an outline with:
- Section headers
- Key points per section
- Approximate length per section
```

### Outline Review Checklist
- [ ] Does the structure flow logically?
- [ ] Are all required topics covered?
- [ ] Is the level of detail appropriate?
- [ ] Does it address the audience's needs?

### Iterate on Outline
```
Adjustments to outline:
- Move [section] before [section]
- Add section on [topic]
- Remove [section] - not needed
- Expand [section] to cover [detail]
```

## Phase 3: Draft Creation

### Section-by-Section Approach
For longer documents, draft one section at a time:

```
Write the [Section Name] section.
Key points to cover:
- [Point 1]
- [Point 2]
Tone: [specific guidance]
Length: [word count]
```

### Full Draft Request
For shorter documents:

```
Write the full draft based on our outline.
Style notes:
- Use active voice
- Keep sentences under 25 words
- Use bullet points for lists of 3+
```

## Phase 4: Refinement

### Feedback Patterns

**Specific changes:**
```
In the [section name]:
- Change [original] to [new]
- Add detail about [topic]
- Remove the paragraph about [topic]
- Strengthen the point about [topic]
```

**Tone adjustment:**
```
The tone is too [formal/casual/technical].
Make it more [conversational/authoritative/accessible].
Specifically, [example of desired change].
```

**Structure changes:**
```
Restructure to:
1. Start with [new opening]
2. Move [section] earlier
3. Combine [sections]
4. Add transition between [sections]
```

**Audience calibration:**
```
This is too [advanced/basic] for the audience.
They already know: [context]
They don't know: [context]
Adjust the level of explanation.
```

## Phase 5: Verification

### Self-Review Checklist
- [ ] Does the opening hook the reader?
- [ ] Is the main point clear within 30 seconds?
- [ ] Does each section serve the goal?
- [ ] Are there clear next steps/call to action?
- [ ] Is the length appropriate?
- [ ] Are there any jargon terms that need explanation?

### Reader Test
```
Review this document as a [role]:
- What questions would they have?
- What's confusing?
- What's missing?
- Would they take the intended action?
```

### Final Polish
```
Final review:
- Fix any grammar/spelling
- Ensure consistent formatting
- Check all names/numbers/dates
- Verify links work (if applicable)
```

## Document Templates

### Technical Spec
```markdown
# [Feature/System Name] Technical Specification

## Overview
[2-3 sentence summary]

## Goals
- Primary: [goal]
- Secondary: [goal]

## Non-Goals
- [Explicitly out of scope]

## Background
[Context needed to understand the proposal]

## Detailed Design
### [Component 1]
[Details...]

### [Component 2]
[Details...]

## Alternatives Considered
| Alternative | Pros | Cons | Why Not |
|-------------|------|------|---------|

## Security Considerations
[Security implications]

## Testing Plan
[How this will be tested]

## Rollout Plan
[How this will be deployed]

## Open Questions
- [ ] [Question 1]
```

### Decision Document
```markdown
# Decision: [Topic]

## Status
[Proposed / Approved / Deprecated]

## Context
[Why is this decision needed?]

## Decision
[What was decided]

## Consequences
### Positive
- [Benefit 1]

### Negative
- [Tradeoff 1]

## Options Considered
1. **[Option 1]** - [Summary]
2. **[Option 2]** - [Summary]
3. **[Option 3]** - [Summary]
```

### Proposal
```markdown
# Proposal: [Title]

## Executive Summary
[One paragraph summary]

## Problem Statement
[What problem are we solving?]

## Proposed Solution
[What do you propose?]

## Benefits
1. [Benefit 1]
2. [Benefit 2]

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|

## Timeline
[Key milestones]

## Resources Required
[What do you need?]

## Success Metrics
[How will we measure success?]

## Recommendation
[Clear ask]
```

## Tips for Effective Co-authoring

1. **Be specific** - Vague feedback leads to vague changes
2. **Share examples** - "Write like [this example]"
3. **Iterate quickly** - Small changes, frequent review
4. **Trust the process** - Outline → Draft → Refine → Polish
5. **Know when to stop** - Perfect is the enemy of done
