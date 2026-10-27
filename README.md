# Rentala Privacy Policy

This repository contains the canonical public-facing privacy policy for the Rentala Android application and informational website. Rentala is an offline-first rental-management app for independent landlords.

## Policy

- Source: [`index.html`](index.html)
- Repository page: <https://github.com/fak3rfac3/rentala-privacy/blob/main/index.html>
- Live GitHub Pages URL: <https://fak3rfac3.github.io/rentala-privacy/>

The policy is automatically validated and deployed to GitHub Pages via GitHub Actions on pushes to `main`.

## Updating the policy

1. Edit `index.html` and update its effective/last-updated dates when the policy changes.
2. Mirror any applicable updates into `src/components/PrivacyPolicy.tsx` in [`fak3rfac3/rentala-web`](https://github.com/fak3rfac3/rentala-web).
3. Ensure `python scripts/validate_policy.py` and the **Validate privacy policy** workflow pass.
4. After deployment completes, verify <https://fak3rfac3.github.io/rentala-privacy/> on mobile and desktop.
5. Update the privacy-policy URL in Google Play Console if the published URL changes.

Keep the policy consistent with the app's actual release behavior. In particular, review local data handling, optional Google Drive backup, billing, permissions, and retention whenever those features change. Never commit OAuth tokens, signing keys, service-account credentials, or user backup files to this repository.

## Local validation

Requires Python 3.10 or newer; no third-party packages are needed.

```powershell
python scripts/validate_policy.py
```

## Contact

- **Developer / Privacy Inquiries:** [Christian Tucay](mailto:ctucay.terre@gmail.com)
- **General Support:** [rentala-support@googlegroups.com](mailto:rentala-support@googlegroups.com)
- **Official Facebook Page:** <https://www.facebook.com/RentalaApp>
