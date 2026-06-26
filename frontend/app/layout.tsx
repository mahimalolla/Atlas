import type { Metadata } from "next";
import "./globals.css";

export const metadata = {
  title: "Atlas | Institutional Knowledge Engine",
  description:
    "Institutional knowledge platform transforming portfolio operating experience into reusable playbooks.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
