import Profile from "@/components/profile";
import { withPageAuthRequired, getSession } from "@auth0/nextjs-auth0";

export default withPageAuthRequired(async function ProfilePage() {
   return (<Profile></Profile>);
}, { returnTo: '/profile' });