# Contributing to Bharat Direct

Bharat Direct is a discussion starter meant to become shared public infrastructure. Critique is as welcome as code — being shown where the idea is wrong is the point.

## Ways to contribute

1. **Challenge the thesis.** Open an issue. Be specific: cite the document and section, name the actor or flow, and describe the failure mode or the better alternative. "This won't work" is less useful than "Section 5 assumes X; here's the case where X breaks."
2. **Improve the protocol.** Proposed changes to `spec/SPEC.md` should preserve the *integration promise* (one API, conformance profiles, federated, easy in/out) and say how the change would be tested.
3. **Build a reference piece.** The merchant connector, the Aware Layer SDK, and the FRC mock are the priority components. Anything that lets someone integrate in a day moves this forward.
4. **Bring evidence.** Any claim about fraud reduction must be measurable. Proposals affecting the Aware Layer should describe how the effect would be measured, not just asserted.

## Ground rules

- **Lead with the fraud win.** It's the safest, most demonstrable entry point and the piece being built first.
- **Keep raw data out.** The FRC design shares *intelligence, not raw PII*. Any contribution touching data flows must respect federated/privacy-preserving principles and the DPDP Act.
- **Primary sources over estimates.** Pin figures to RBI / NPCI / PIB where possible; mark secondary estimates as such.

## Who we especially want to hear from

Banks, PSPs, fraud and risk teams, behavioural-science and security researchers, and potential anchor owners. If that's you, reach out: **dhirendrasrajput@gmail.com**.

## Licensing of contributions

By contributing you agree your contributions are licensed under the repository's terms: **CC BY 4.0** for specification and documents, **Apache-2.0** for code.
