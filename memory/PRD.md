# P&D AGENCY — Landing Page

## Original Problem Statement
Build a landing page for "P&D AGENCY" web development agency that closely emulates (~95%) a provided dark brutalist HTML reference design. Portuguese language, no prices in packages section, contact form modal integrated.

## User Choices
- Language: Portuguese
- Package CTAs: "SOLICITAR ORÇAMENTO" for both packages (no prices shown)
- Contact buttons: Open integrated modal form
- Branding: Keep "P&D AGENCY" and placeholder content

## Architecture
- **Frontend**: React (CRA + CRACO) — single-page landing page
- **Backend**: FastAPI — contact form submission endpoint
- **Database**: MongoDB — stores contact form submissions

## What's Been Implemented (2026-04-15)
- Full dark brutalist landing page in Portuguese (95% fidelity to reference)
- Glassmorphism sticky header with nav links
- Hero section with cyan glow effects and animated entrance
- Services section (2 cards: Desenvolvimento Web + Expansão Mobile)
- Portfolio bento grid (2 image cards: NEON LEDGER + VELVET VOID)
- Packages section — NO prices, both with "SOLICITAR ORÇAMENTO" CTA
- Final CTA section ("PRONTO PARA TRANSCENDER?")
- Footer with nav + social links
- Contact form modal (Shadcn Dialog) with fields: Nome, Email, Pacote de Interesse, Mensagem
- Package pre-selection in modal when clicking specific package CTA
- Backend POST /api/contact endpoint saves to MongoDB
- Backend GET /api/contact endpoint to retrieve submissions

## Color System
- Primary: #81ecff (cyan)
- Secondary: #bc87fe (purple)
- Background: #0e0e0e
- Surface: #1a1a1a / #131313 / #2c2c2c
- Text secondary: #adaaaa

## Fonts
- Headlines: Space Grotesk
- Body/Labels: Manrope
- Icons: Material Symbols Outlined (Google Fonts CDN)

## Test Results (iteration_1)
- Backend: 100% pass
- Frontend: 100% pass
- All 5 CTA buttons open modal
- Package pre-selection works
- Form submission + success message verified

## Prioritized Backlog

### P1 (Next Priority)
- Add real social media links
- Add email notification on contact form submission
- SEO meta tags and Open Graph

### P2
- Admin panel to view contact submissions
- Real portfolio projects
- Testimonials section
- Multi-language support (EN/PT toggle)

### P3
- Cookie consent banner
- Analytics integration
- Blog/case studies section
