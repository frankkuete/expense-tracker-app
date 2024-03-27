import Profile from "@/components/profile";
import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Hello
      <a href="/api/auth/login">Login</a>
      <a href="/api/auth/logout">Logout</a>
    </main>
  );
}
